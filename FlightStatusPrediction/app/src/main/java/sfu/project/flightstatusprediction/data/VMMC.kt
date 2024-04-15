package sfu.project.flightstatusprediction.data

data class VMMC(
    val distance: Double,
    val latitude: Double,
    val longitude: Double,
    val useCount: Int,
    val id: String,
    val name: String,
    val quality: Int,
    val contribution: Int
)
