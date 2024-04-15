package sfu.project.flightstatusprediction.data

data class DeparturePassFlightInfo(
    val time: String,
    val flight: List<FlightInfoItem>,
    val status: String ?= null,
    val statusCode: String ?= null,
    val destination: List<String>,
    val terminal: String ?= null,
    val aisle: String ?= null,
    val gate: String ?= null
)
