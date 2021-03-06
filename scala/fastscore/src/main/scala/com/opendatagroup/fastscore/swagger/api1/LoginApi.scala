/**
 * FastScore API (proxy)
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.6
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package com.opendatagroup.fastscore.swagger.api1

import com.opendatagroup.fastscore.swagger.invoker1.ApiInvoker
import com.opendatagroup.fastscore.swagger.invoker1.ApiException

import com.sun.jersey.multipart.FormDataMultiPart
import com.sun.jersey.multipart.file.FileDataBodyPart

import javax.ws.rs.core.MediaType

import java.io.File
import java.util.Date

import scala.collection.mutable.HashMap

class LoginApi(val defBasePath: String = "https://localhost/api/1/service",
                        defApiInvoker: ApiInvoker = ApiInvoker) {
  var basePath = defBasePath
  var apiInvoker = defApiInvoker

  def addHeader(key: String, value: String) = apiInvoker.defaultHeaders += key -> value 

  /**
   * 
   * 
   * @param username user name 
   * @param password password 
   * @return void
   */
  def loginPost(username: String, password: String) = {
    // create path and map variables
    val path = "/1/login".replaceAll("\\{format\\}", "json")

    val contentTypes = List("application/x-www-form-urlencoded")
    val contentType = contentTypes(0)

    val queryParams = new HashMap[String, String]
    val headerParams = new HashMap[String, String]
    val formParams = new HashMap[String, String]

    if (username == null) throw new Exception("Missing required parameter 'username' when calling LoginApi->loginPost")

    if (password == null) throw new Exception("Missing required parameter 'password' when calling LoginApi->loginPost")

    

    var postBody:AnyRef = null.asInstanceOf[AnyRef]

    if (contentType.startsWith("multipart/form-data")) {
      val mp = new FormDataMultiPart
      mp.field("username", username.toString, MediaType.MULTIPART_FORM_DATA_TYPE)
      mp.field("password", password.toString, MediaType.MULTIPART_FORM_DATA_TYPE)
      postBody = mp
    } else {
      formParams += "username" -> username.toString
      formParams += "password" -> password.toString
    }

    try {
      apiInvoker.invokeApi(basePath, path, "POST", queryParams.toMap, formParams.toMap, postBody, headerParams.toMap, contentType) match {
        case s: String =>
                  case _ => None
      }
    } catch {
      case ex: ApiException if ex.code == 404 => None
      case ex: ApiException => throw ex
    }
  }

}
