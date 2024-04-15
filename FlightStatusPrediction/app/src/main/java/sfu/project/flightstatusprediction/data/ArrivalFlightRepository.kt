package sfu.project.flightstatusprediction.data

import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.launch

class ArrivalFlightRepository(private val arrivalFlightDatabaseDao: ArrivalFlightDatabaseDao) {

    val allArrivalFlights: Flow<List<DBArrFlightInfo>> = arrivalFlightDatabaseDao.getAllArrivalFlights()

    fun getArrivalFlightsAt(date: String): Flow<List<DBArrFlightInfo>>{
        return arrivalFlightDatabaseDao.getArrivalFlightsAt(date)
    }

    fun insert(arrivalFlight: DBArrFlightInfo){
        CoroutineScope(IO).launch{
            arrivalFlightDatabaseDao.insertFlight(arrivalFlight)
        }
    }

    fun delete(id: Long){
        CoroutineScope(IO).launch {
            arrivalFlightDatabaseDao.deleteArrivalFlight(id)
        }
    }

    fun deleteAll(){
        CoroutineScope(IO).launch{
            arrivalFlightDatabaseDao.deleteAll()
        }
    }
}