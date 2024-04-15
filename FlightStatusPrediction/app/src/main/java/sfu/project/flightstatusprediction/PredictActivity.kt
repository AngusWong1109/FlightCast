package sfu.project.flightstatusprediction

import android.content.res.AssetManager
import android.os.Bundle
import android.os.FileUtils
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.chaquo.python.PyObject
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import sfu.project.flightstatusprediction.data.TripInfo
import java.io.File

class PredictActivity : AppCompatActivity() {
    private val py: Python
    private val joblib: PyObject
    private val np: PyObject
    private val sk: PyObject
    private lateinit var assetManager: AssetManager
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        assetManager = this.applicationContext.assets
    }
    init{
        if(! Python.isStarted()){
            Python.start(AndroidPlatform(this))
        }
        py = Python.getInstance()
        joblib = py.getModule("joblib")
        np = py.getModule("numpy")
        sk = py.getModule("sklearn.preprocessing")
    }

    fun extractFile(fileName: String){
        val inputStream = assetManager.open(fileName)
        val file = File(fileName)
    }

    fun arrival_predict(data: TripInfo){
        val arr = np.callAttr("array", data)

    }

    fun departure_predict(data: TripInfo){
        
    }
}