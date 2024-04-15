package sfu.project.flightstatusprediction.data

data class TripInfo(
    val time: String = "",
    val flightNo: String ?= "",
    val airline: String ?= "",
    val place: String ?= "",
    val temp: Double = 0.0,
    val feelsLike: Double = 0.0,
    val dew: Double = 0.0,
    val humidity: Double = 0.0,
    val precip: Double ?= 0.0,
    val precipProb: Double ?= 0.0,
    val windGust: Double = 0.0,
    val windSpeed: Double = 0.0,
    val windDir: Double = 0.0,
    val pressure: Double = 0.0,
    val cloudCover: Double = 0.0,
    val visibility: Double = 0.0,
    val solarRadiation: Double = 0.0,
    val solarEnergy: Double = 0.0,
    val uvIndex: Double = 0.0,
    val severeRisk: Double = 0.0,
    val conditions: String = ""
)
