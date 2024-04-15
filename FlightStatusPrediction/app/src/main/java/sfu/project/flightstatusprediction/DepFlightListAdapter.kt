package sfu.project.flightstatusprediction

import android.app.Activity
import android.content.Intent
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import sfu.project.flightstatusprediction.data.DBDepFlightInfo

class DepFlightListAdapter(): RecyclerView.Adapter<FlightViewHolder>() {
    companion object{
        var flights: List<DBDepFlightInfo> = ArrayList()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): FlightViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.flight_list_recycler_view_layout, parent, false)
        return FlightViewHolder(view)
    }

    override fun getItemCount(): Int {
        return flights.size
    }

    override fun onBindViewHolder(holder: FlightViewHolder, position: Int) {
        val depFlightListInfo = flights[position]
        holder.tvTime.text = depFlightListInfo.time
        holder.tvFlightNo.text = depFlightListInfo.flightNo
        holder.tvStatus.text = depFlightListInfo.status
        holder.tvPlace.text = depFlightListInfo.destination
        val activity = holder.itemView.context as Activity
        holder.itemView.setOnClickListener {
            val intent = Intent(activity, DepartureShowFlightInfoActivity::class.java)
            intent.putExtra(DepartureShowFlightInfoActivity.DEPARTURE_EXTRA_POSITION, position)
            activity.startActivity(intent)
        }
    }

    fun replace(newFlights: List<DBDepFlightInfo>){
        flights = newFlights
    }
}