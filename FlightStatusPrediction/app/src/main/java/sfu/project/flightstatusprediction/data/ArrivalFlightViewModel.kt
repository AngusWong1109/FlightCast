package sfu.project.flightstatusprediction.data

import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.asLiveData
import kotlinx.coroutines.flow.Flow
import sfu.project.flightstatusprediction.GetFlightInfo
import sfu.project.flightstatusprediction.GetFlightInfo.ArrFlightInfoResponse
import java.time.LocalDate
import java.time.format.DateTimeFormatter

class ArrivalFlightViewModel(private val repository: ArrivalFlightRepository) : ViewModel() {
//    val allArrFlightsLiveData: LiveData<List<DBArrFlightInfo>> = repository.allArrivalFlights.asLiveData()
    var arrFlightsByDate: LiveData<List<DBArrFlightInfo>>

    init{
        val today = LocalDate.now()
        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
        val dateStr = today.plusDays(1).format(formatter)
        arrFlightsByDate = repository.getArrivalFlightsAt(dateStr).asLiveData()
    }

    fun insert(flight: ArrFlightInfoResponse){
        for (flightInfo in flight.list){
            val arrFlight = DBArrFlightInfo()
            arrFlight.date = flight.date
            arrFlight.arrival = flight.arrival
            arrFlight.cargo = flight.cargo
            arrFlight.time = flightInfo.time
            arrFlight.flightNo = flightInfo.flight.joinToString { it.no }
            arrFlight.airline = flightInfo.flight.joinToString { it.airline }
            arrFlight.status = flightInfo.status
            arrFlight.statusCode = flightInfo.statusCode
            arrFlight.origin = flightInfo.origin.joinToString()
            arrFlight.baggage = flightInfo.baggage
            arrFlight.hall = flightInfo.hall
            arrFlight.terminal = flightInfo.terminal
            arrFlight.stand = flightInfo.stand
            repository.insert(arrFlight)
        }
    }

    fun getArrivalFlightsAt(date: String){
        arrFlightsByDate = repository.getArrivalFlightsAt(date).asLiveData()
    }

    /*
    fun deleteFirst(){
        val arrFlightList = allArrFlightsLiveData.value
        if (!arrFlightList.isNullOrEmpty()){
            val id = arrFlightList[0].id
            repository.delete(id)
        }
    }
    */

    /*
    fun deleteAll(){
        val arrFlightList = allArrFlightsLiveData.value
        if(!arrFlightList.isNullOrEmpty()){
            repository.deleteAll()
        }
    }
    */
}

class ArrivalFlightViewModelFactory (private val repository: ArrivalFlightRepository) : ViewModelProvider.Factory{
    override fun<T: ViewModel> create(modelClass: Class<T>) : T{
        if(modelClass.isAssignableFrom(ArrivalFlightViewModel::class.java))
            return ArrivalFlightViewModel(repository) as T
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}