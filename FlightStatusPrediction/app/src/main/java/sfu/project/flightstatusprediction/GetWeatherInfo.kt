package sfu.project.flightstatusprediction

import android.util.Log
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import sfu.project.flightstatusprediction.data.WeatherDailyInfo
import sfu.project.flightstatusprediction.data.WeatherStationInfo
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL

class GetWeatherInfo {
    fun getWeather(): WeatherResponse?{
        val endpoint = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Hong%20Kong%20International%20Airport?unitGroup=metric&include=hours&key=3TX3Y9V92EQVZ7SG4ZT6PKEDW&contentType=json"
        val url = URL(endpoint)
        val openedConnection = url.openConnection() as HttpURLConnection
        openedConnection.requestMethod = "GET"

        val responseCode = openedConnection.responseCode
        return try{
            val reader = BufferedReader(InputStreamReader(openedConnection.inputStream))
            val response = reader.readText()
            val apiResponse = ApiResponse(
                responseCode,
                weatherParseJson(response)
            )
            reader.close()
            apiResponse.response
        }catch(e: Exception){
            Log.e("Weather data fetch error", e.message.toString())
            null
        }finally{
            openedConnection.disconnect()
        }
    }

    private fun weatherParseJson(text: String): WeatherResponse{
        val gson = Gson()
        val weatherInfo = object : TypeToken<WeatherResponse>() {}.type
        return gson.fromJson(text, weatherInfo)
    }

    data class ApiResponse(
        val responseCode: Int,
        val response: WeatherResponse
    )

    data class WeatherResponse(
        val queryCost: Int,
        val latitude: Float,
        val longitude: Float,
        val resolvedAddress: String,
        val address: String,
        val timezone: String,
        val tzoffset: Int,
        val days: List<WeatherDailyInfo>,
        val stations: WeatherStationInfo
    )
}