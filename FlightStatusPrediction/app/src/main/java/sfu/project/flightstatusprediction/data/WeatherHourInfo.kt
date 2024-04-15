package sfu.project.flightstatusprediction.data

data class WeatherHourInfo(
    val datetime: String,
    val datetimeEpoch: Long,
    val temp: Double,
    val feelslike: Double,
    val humidity: Double,
    val dew: Double,
    val precip: Double,
    val precipprob: Double,
    val snow: Double,
    val snowdepth: Double? = null,
    val precitype: String? = null,
    val windgust: Double,
    val windspeed: Double,
    val winddir: Double,
    val pressure: Double,
    val visibility: Double,
    val cloudcover: Double,
    val solarradiation: Double,
    val solarenergy: Double,
    val uvindex: Double,
    val severerisk: Double,
    val conditions: String,
    val icon: String,
    val stations: List<String>,
    val source: String
)
