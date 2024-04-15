package sfu.project.flightstatusprediction

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import sfu.project.flightstatusprediction.GetFlightInfo.Companion.days
import sfu.project.flightstatusprediction.GetFlightInfo.Companion.today
import sfu.project.flightstatusprediction.data.ArrivalFlightDatabase
import sfu.project.flightstatusprediction.data.ArrivalFlightDatabaseDao
import sfu.project.flightstatusprediction.data.ArrivalFlightRepository
import sfu.project.flightstatusprediction.data.ArrivalFlightViewModel
import sfu.project.flightstatusprediction.data.ArrivalFlightViewModelFactory
import sfu.project.flightstatusprediction.data.DBDepFlightInfo
import sfu.project.flightstatusprediction.data.DepartureFlightDatabase
import sfu.project.flightstatusprediction.data.DepartureFlightDatabaseDao
import sfu.project.flightstatusprediction.data.DepartureFlightRepository
import sfu.project.flightstatusprediction.data.DepartureFlightViewModel
import sfu.project.flightstatusprediction.data.DepartureFlightViewModelFactory
import java.time.format.DateTimeFormatter

class FlightDepartureListFragment : Fragment() {
    private lateinit var rvDate: RecyclerView
    private lateinit var rvFlight: RecyclerView
    private lateinit var tvDateSelected: TextView

    private lateinit var arrFlightDb: ArrivalFlightDatabase
    private lateinit var arrFlightDbDao: ArrivalFlightDatabaseDao
    private lateinit var arrFlightRepository: ArrivalFlightRepository
    private lateinit var arrFlightViewModelFactory: ArrivalFlightViewModelFactory
    private lateinit var arrFlightViewModel: ArrivalFlightViewModel

    private lateinit var depFlightDb: DepartureFlightDatabase
    private lateinit var depFlightDbDao: DepartureFlightDatabaseDao
    private lateinit var depFlightRepository: DepartureFlightRepository
    private lateinit var depFlightViewModelFactory: DepartureFlightViewModelFactory
    private lateinit var depFlightViewModel: DepartureFlightViewModel

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val ret = inflater.inflate(R.layout.fragment_flight_departure_list, container, false)
        rvDate = ret.findViewById(R.id.rv_dep_date)
        rvFlight = ret.findViewById(R.id.rv_dep_flight)
        tvDateSelected = ret.findViewById(R.id.tv_dep_date_selected)

        arrFlightDb = ArrivalFlightDatabase.getInstance(requireActivity())
        arrFlightDbDao = arrFlightDb.arrivalFlightDatabaseDao
        arrFlightRepository = ArrivalFlightRepository(arrFlightDbDao)
        arrFlightViewModelFactory = ArrivalFlightViewModelFactory(arrFlightRepository)
        arrFlightViewModel = ViewModelProvider(this, arrFlightViewModelFactory).get(ArrivalFlightViewModel::class.java)

        depFlightDb = DepartureFlightDatabase.getInstance(requireActivity())
        depFlightDbDao = depFlightDb.departureFlightDatabaseDao
        depFlightRepository = DepartureFlightRepository(depFlightDbDao)
        depFlightViewModelFactory = DepartureFlightViewModelFactory(depFlightRepository)
        depFlightViewModel = ViewModelProvider(this, depFlightViewModelFactory).get(DepartureFlightViewModel::class.java)

        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
        val dateString = today.plusDays(1).format(formatter)
        tvDateSelected.text = dateString

        val dateAdapter = DateAdapter(days, tvDateSelected, false, arrFlightViewModel, depFlightViewModel)
        rvDate.adapter = dateAdapter
        val layoutManager = LinearLayoutManager(activity, RecyclerView.HORIZONTAL, false)
        rvDate.layoutManager = layoutManager

        val flightAdapter = DepFlightListAdapter()
        rvFlight.adapter = flightAdapter

        depFlightViewModel.depFlightsByDate.observe(requireActivity(), Observer { it ->
            Log.i("Departure observer", it.toString())
            flightAdapter.replace(it)
            flightAdapter.notifyDataSetChanged()
        })

        val flightLayoutManager = LinearLayoutManager(activity, RecyclerView.VERTICAL, false)
        rvFlight.layoutManager = flightLayoutManager
        return ret
    }
}