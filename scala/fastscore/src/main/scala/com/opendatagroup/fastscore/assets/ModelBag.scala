package com.opendatagroup.fastscore.assets

import com.opendatagroup.fastscore.fleet.ModelManage
import com.opendatagroup.fastscore.util._
import com.opendatagroup.fastscore.assets.Constants._

/** A live collection of models in ModelManage
  *
  * @param mm ModelManage instance
  */
class ModelBag(mm: ModelManage) extends Bag[ModelMetadata, Model] {
    val modelmanage = mm

    /** Returns a list of model names
      *
      * @return list of model names
      */
    def names(): List[String] = mm.v1.modelList(mm.toString) match {
        case Some(models) => models.map(_.toString)
        case None => List()
    }

    /** Save a model to ModelManage
      *
      * @param name model name in ModelManage
      * @param model model object
      */
    def put(name: String, model: Model): Unit = {
        modelmanage.v1.modelPut(modelmanage.toString, name, model.toString, MODEL_CONTENT_TYPES.get(model.format))
    }

    /** List of models
      *
      * @return list of models
      */
    def iterator = {
        mm.v1.modelList(mm.toString, Some("type")) match {
            case Some(models) =>
                models.iterator
                .map { case m: Map[String, String] => (m.get("name"), m.get("type")) match {
                    case (Some(name), Some(format)) => ModelMetadata(name, format.toLowerCase, mm)
                    case _ => throw FastScoreError("Unexpected response from ModelManage")
                }}
            case None => throw FastScoreError("Unexpected response from ModelManage")
        }
    }
}
