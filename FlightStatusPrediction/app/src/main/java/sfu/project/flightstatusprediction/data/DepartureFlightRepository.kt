package sfu.project.flightstatusprediction.data

import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.launch

class DepartureFlightRepository(private val departureFlightDatabaseDao: DepartureFlightDatabaseDao){

    val allDepartureFlights: Flow<List<DBDepFlightInfo>> = departureFlightDatabaseDao.getAllDepartureFlights()

    fun getDepartureFlightsAt(date: String): Flow<List<DBDepFlightInfo>>{
        return departureFlightDatabaseDao.getDepartureFlightsAt(date)
    }

    fun insert(departureFlight: DBDepFlightInfo){
        CoroutineScope(IO).launch{
            departureFlightDatabaseDao.insertFlight(departureFlight)
        }
    }

    fun delete(id: Long){
        CoroutineScope(IO).launch{
            departureFlightDatabaseDao.deleteDepartureFlight(id)
        }
    }

    fun deleteAll(){
        CoroutineScope(IO).launch{
            departureFlightDatabaseDao.deleteAll()
        }
    }
}