
import json
from iso8601 import parse_date
from websocket import create_connection, WebSocketTimeoutException
from ssl import CERT_NONE

from .errors import FastScoreError

PNEUMO_WS_PATH = '/api/1/service/connect/1/notify'

class PneumoSock(object):
    """
    The Pneumo websocket.

    >>> pneumo = connect.pneumo()
    >>> pneumo.recv()
    LogMsg(src=..., timestamp=..., ...)

    .. todo::

       Add __str__() methods to all Pneumo messages.

    """
    def __init__(self, proxy_prefix, timeout=None):
        url = proxy_prefix.replace('https:', 'wss:') + PNEUMO_WS_PATH
        self._ws = create_connection(url, sslopt = {'cert_reqs': CERT_NONE})
        if timeout != None:
            self._ws.settimeout(timeout)

    def recv(self):
        """
        Receives the next Pneumo message.

        """
        return PneumoSock.make_message(json.loads(self._ws.recv()))

    def close(self):
        """
        Close the Pneumo socket.
        """
        self._ws.close()

    @staticmethod
    def make_message(data):
        src = data['src']
        timestamp = data['timestamp']
        ptype = data['type']
        if ptype == 'health':
            return HealthMsg(src, timestamp, data['instance'], data['health'])
        elif ptype == 'log':
            return LogMsg(src, timestamp, data['level'], data['text'])
        elif ptype == 'model-console':
            return ModelConsoleMsg(src, timestamp, data['text'])
        elif ptype == 'engine-state':
            return EngineStateMsg(src, timestamp, data['state'])
        elif ptype == 'engine-config':
            return EngineConfigMsg(src, timestamp, data['item'], data['op'], data.get('ref'))
        elif ptype == 'sensor-report':
            return SensorReportMsg(src, timestamp, data['id'], data['tap'], data['data'])
        else:
            raise FastScoreError("Unexpected Pneumo message type '%s'" % ptype)

class PneumoMsg(object):
    def __init__(self, src, timestamp):
        self._src = src
        self._timestamp = parse_date(timestamp)

    @property
    def src(self):
        return self._src

    @property
    def timestamp(self):
        return self._timestamp

    def __repr__(self):
        return "PneumoMsg(src=%s, timestamp=%s)" % (self.src,self.timestamp)

class HealthMsg(PneumoMsg):
    def __init__(self, src, timestamp, instance, health):
        super(HealthMsg, self).__init__(src, timestamp)
        self._instance = instance
        self._health = health

    @property
    def instance(self):
        return self._instance

    @property
    def health(self):
        return self._health

    def __str__(self):
        if self._health == 'ok':
            updown = "up"
        elif self._health == 'fail':
            updown = "DOWN"
        else:
            updown = self._health
        
        return "%s is %s" % (self._instance,updown)

    def __repr__(self):
        return "HealthMsg(src=%s, timestamp=%s, instance=%s, health=%s)" \
                    % (self.src,self.timestamp,self.instance,self.health)

class LogMsg(PneumoMsg):

    LAGER_LEVELS = {
        128: 'debug',
        64: 'info',
        32: 'notice',
        16: 'warning',
        8: 'error',
        4: 'critical',
        2: 'alert',
        1: 'emergency',
    }

    def __init__(self, src, timestamp, level, text):
        super(LogMsg, self).__init__(src, timestamp)
        self._level = level
        self._text = text

    @property
    def level(self):
        return self._level

    @property
    def text(self):
        return self._text

    def __str__(self):
        severity = LogMsg.LAGER_LEVELS[self._level] \
                    if self._level in LogMsg.LAGER_LEVELS else self._level
        return "log[%s] %s" % (severity,self._text)

    def __repr__(self):
        return "LogMsg(src=%s, timestamp=%s, level=%s, text=%s)" \
                    % (self.src,self.timestamp,self.level,self.text.replace('\n', '\\n'))

class ModelConsoleMsg(PneumoMsg):
    def __init__(self, src, timestamp, text):
        super(ModelConsoleMsg, self).__init__(src, timestamp)
        self._text = text

    @property
    def text(self):
        return self._text

    def __str__(self):
        return "console: %s" % self._text.rstrip()

    def __repr__(self):
        return "ModelConsoleMsg(src=%s, timestamp=%s, text=%s)" \
                    % (self.src,self.timestamp,self.text.replace('\n', '\\n'))

class EngineStateMsg(PneumoMsg):
    def __init__(self, src, timestamp, state):
        super(EngineStateMsg, self).__init__(src, timestamp)
        self._state = state

    @property
    def state(self):
        return self._state

    def __str__(self):
        return "state is %s" % self._state.upper()

    def __repr__(self):
        return "EngineState(src=%s, timestamp=%s, state=%s)" \
                    % (self.src,self.timestamp,self.state.upper())

class EngineConfigMsg(PneumoMsg):
    def __init__(self, src, timestamp, item, op, ref=None):
        super(EngineConfigMsg, self).__init__(src, timestamp)
        self._item = item
        self._op   = op
        self._ref = ref

    @property
    def item(self):
        return self._item

    @property
    def op(self):
        return self._op

    @property
    def ref(self):
        return self._ref

    def __str__(self):
        if self._item == 'model':
            if self._op == 'load':
                return "model loaded"
            elif self._op == 'reload':
                return "model reloaded"
            elif self._op == 'unload':
                return "model unloaded"
        elif self._item == 'stream':
            if self._op == 'attach':
                return "stream attached to %d" % self._ref
            elif self._op == 'reattach':
                return "stream reattached to %d" % self._ref
            elif self._op == 'detach':
                return "stream detached from %d" % self._ref
        elif self._item == 'jet':
            if self._op == 'start':
                return "jet started (%s)" % self._ref
            elif self._op == 'stop':
                return "jet stoppped (%s)" % self._ref
        return repr(self)

    def __repr__(self):
        return "EngineConfig(src=%s, timestamp=%s, item=%s, op=%s, ref=%s)" \
                    % (self.src,self.timestamp,self.item,self.op,self.ref)

class SensorReportMsg(PneumoMsg):
    def __init__(self, src, timestamp, sid, point, data):
        super(SensorReportMsg, self).__init__(src, timestamp)
        self._sid   = sid
        self._point = point
        self._data  = data

    @property
    def sid(self):
        return self._sid

    @property
    def point(self):
        return self._point

    @property
    def data(self):
        return self._data

    def __str__(self):
        return "sensor[%d] %s: %s" % (self.sid,self.point,repr(self.data))

    def __repr__(self):
        return "SensorReportMsg(src=%s, timestamp=%s, sid=%d, point=%s, data=%s)" \
                    % (self.src,self.timestamp,self.sid,self.point,repr(self.data))
