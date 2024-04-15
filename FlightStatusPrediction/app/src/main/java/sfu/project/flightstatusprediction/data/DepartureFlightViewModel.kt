package sfu.project.flightstatusprediction.data

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.asLiveData
import sfu.project.flightstatusprediction.GetFlightInfo
import java.lang.IllegalArgumentException
import java.time.LocalDate
import java.time.format.DateTimeFormatter

class DepartureFlightViewModel(private val repository: DepartureFlightRepository) : ViewModel() {
//    val allDepFlightsLiveData: LiveData<List<DBDepFlightInfo>> = repository.allDepartureFlights.asLiveData()
    var depFlightsByDate: LiveData<List<DBDepFlightInfo>>

    init{
        val today = LocalDate.now()
        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
        val dateStr = today.plusDays(1).format(formatter)
        depFlightsByDate = repository.getDepartureFlightsAt(dateStr).asLiveData()
    }

    fun insert(flight: GetFlightInfo.DepFlightInfoResponse){
        Log.i("departure flight: ", flight.toString())
        for (flightInfo in flight.list){
            val depFlight = DBDepFlightInfo()
            depFlight.date = flight.date
            depFlight.arrival = flight.arrival
            depFlight.cargo = flight.cargo
            depFlight.time = flightInfo.time
            depFlight.flightNo = flightInfo.flight.joinToString { it.no }
            depFlight.airline = flightInfo.flight.joinToString { it.airline }
            depFlight.status = flightInfo.status
            depFlight.statusCode = flightInfo.statusCode
            depFlight.destination = flightInfo.destination.joinToString()
            depFlight.terminal = flightInfo.terminal
            depFlight.aisle = flightInfo.aisle
            depFlight.gate = flightInfo.gate
            repository.insert(depFlight)
        }
    }

    fun getDepartureFlightAt(date: String){
        depFlightsByDate = repository.getDepartureFlightsAt(date).asLiveData()
    }

    /*
    fun deleteFirst(){
        val depFlightList = allDepFlightsLiveData.value
        if(!depFlightList.isNullOrEmpty()){
            val id = depFlightList[0].id
            repository.delete(id)
        }
    }

    fun deleteAll(){
        val depFlightList = allDepFlightsLiveData.value
        if(!depFlightList.isNullOrEmpty()){
            repository.deleteAll()
        }
    }
    */
}

class DepartureFlightViewModelFactory (private val repository: DepartureFlightRepository) : ViewModelProvider.Factory{
    override fun<T: ViewModel> create(modelClass: Class<T>) : T{
        if(modelClass.isAssignableFrom(DepartureFlightViewModel::class.java))
            return DepartureFlightViewModel(repository) as T
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}