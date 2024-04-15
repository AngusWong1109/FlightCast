package sfu.project.flightstatusprediction.data

data class ArrivalPassFlightInfo(
    val time: String,
    val flight: List<FlightInfoItem>,
    val status: String ?= null,
    val statusCode: String ?= null,
    val origin: List<String>,
    val baggage: String ?= null,
    val hall: String ?= null,
    val terminal: String ?= null,
    val stand: String ?= null
)
