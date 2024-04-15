package sfu.project.flightstatusprediction

import android.util.Log
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.launch
import sfu.project.flightstatusprediction.data.ArrivalFlightViewModel
import sfu.project.flightstatusprediction.data.ArrivalPassFlightInfo
import sfu.project.flightstatusprediction.data.DepartureFlightViewModel
import sfu.project.flightstatusprediction.data.DeparturePassFlightInfo
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL
import java.time.LocalDate
import java.time.format.DateTimeFormatter

//Code adopted from https://www.mobileinsights.dev/making-get-requests-to-a-rest-api-with-kotlin-and-gson-in-android-9005ef75546e

class GetFlightInfo {
    companion object{
        val today: LocalDate = LocalDate.now()
        val startDate: LocalDate = today.plusDays(1)
        val endDate: LocalDate = today.plusDays(14)
        val days = ArrayList<LocalDate>()
        init{
            var day = startDate
            while(day.isBefore(endDate)){
                days.add(day)
                day = day.plusDays(1)
            }
        }
    }

    fun fetchAllFlight(depViewModel: DepartureFlightViewModel, arrViewModel: ArrivalFlightViewModel){
        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
        var date = startDate
        while(date.isBefore(endDate)){
            val dateStr = date.format(formatter)
            CoroutineScope(IO).launch{
                depViewModel.insert(getPassDep(dateStr)!![0])
                arrViewModel.insert(getPassArr(dateStr)!![0])
            }
            date = date.plusDays(1)
        }

    }

    fun getPassDep(dateStr: String) : ArrayList<DepFlightInfoResponse>?{
        val endpoint = "https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date=$dateStr&lang=en&cargo=false&arrival=false"
        val url = URL(endpoint)
        val openedConnection = url.openConnection() as HttpURLConnection
        openedConnection.requestMethod = "GET"

        val responseCode = openedConnection.responseCode
        return try{
            val reader = BufferedReader(InputStreamReader(openedConnection.inputStream))
            val response = reader.readText()
            val apiResponse = DepApiResponse(
                responseCode,
                depParseJson(response)
            )
            reader.close()
            apiResponse.response as ArrayList<DepFlightInfoResponse>
        } catch(e: Exception){
            Log.e("DataFetching Error", e.message.toString())
            null
        } finally{
            openedConnection.disconnect()
        }
    }

    fun getPassArr(dateStr: String) : ArrayList<ArrFlightInfoResponse>?{
        val endpoint = "https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date=$dateStr&lang=en&cargo=false&arrival=true"
        val url = URL(endpoint)
        val openedConnection = url.openConnection() as HttpURLConnection
        openedConnection.requestMethod = "GET"

        val responseCode = openedConnection.responseCode
        return try{
            val reader = BufferedReader(InputStreamReader(openedConnection.inputStream))
            val response = reader.readText()
            val apiResponse = ArrApiResponse(
                responseCode,
                arrParseJson(response)
            )
            reader.close()
            apiResponse.response as ArrayList<ArrFlightInfoResponse>
        } catch(e: Exception){
            Log.e("ArrivalDataFetchingError", e.message.toString())
            null
        } finally{
            openedConnection.disconnect()
        }
    }

    private fun depParseJson(text: String): List<DepFlightInfoResponse> {
        val gson = Gson()
        val flightInfo = object : TypeToken<List<DepFlightInfoResponse>>() {}.type
        return gson.fromJson(text, flightInfo)
    }

    private fun arrParseJson(text: String): List<ArrFlightInfoResponse>{
        val gson = Gson()
        val flightInfo = object : TypeToken<List<ArrFlightInfoResponse>>() {}.type
        return gson.fromJson(text, flightInfo)
    }

    data class DepApiResponse(
        val responseCode: Int,
        val response: List<DepFlightInfoResponse>
    )

    data class ArrApiResponse(
        val responseCode: Int,
        val response: List<ArrFlightInfoResponse>
    )

    data class DepFlightInfoResponse(
        val date: String,
        val arrival: Boolean,
        val cargo: Boolean,
        val list: List<DeparturePassFlightInfo>
    )

    data class ArrFlightInfoResponse(
        val date: String,
        val arrival: Boolean,
        val cargo: Boolean,
        val list: List<ArrivalPassFlightInfo>
    )
}