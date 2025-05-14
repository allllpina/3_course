package com.example.lab3

import android.os.Bundle
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {

    private lateinit var filterGenreSpinner: Spinner
    private lateinit var ratingSeekBar: SeekBar
    private lateinit var seekbarValue: TextView
    private var selectedGenre: String = "Усі"
    private var minRating: Int = 0

    private lateinit var adapter: BookAdapter
    private val bookList = mutableListOf<Book>()
    private val filteredList = mutableListOf<Book>() // для відображення

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val recyclerView = findViewById<RecyclerView>(R.id.bookRecyclerView)
        adapter = BookAdapter(filteredList) { book ->
            BookDialogFragment(book).show(supportFragmentManager, "BookDialog")
        }
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = adapter

        // Вхідні поля
        val titleInput = findViewById<EditText>(R.id.titleEditText)
        val authorInput = findViewById<EditText>(R.id.authorEditText)
        val reviewInput = findViewById<EditText>(R.id.reviewEditText)
        val ratingBar = findViewById<RatingBar>(R.id.ratingBar)

        val genreFiction = findViewById<CheckBox>(R.id.genreFiction)
        val genreScience = findViewById<CheckBox>(R.id.genreScience)
        val genreBio = findViewById<CheckBox>(R.id.genreBiography)

        // Кнопка додавання
        findViewById<Button>(R.id.addBookButton).setOnClickListener {
            val title = titleInput.text.toString()
            val author = authorInput.text.toString()
            val review = reviewInput.text.toString()
            val rating = ratingBar.rating
            val genres = listOfNotNull(
                if (genreFiction.isChecked) "Фікшн" else null,
                if (genreScience.isChecked) "Наука" else null,
                if (genreBio.isChecked) "Біографія" else null
            )

            if (title.isNotEmpty() && author.isNotEmpty()) {
                val book = Book(title, author, review, rating, genres)
                bookList.add(book)

                applyFilters()

                titleInput.text.clear()
                authorInput.text.clear()
                reviewInput.text.clear()
                ratingBar.rating = 0f
                genreFiction.isChecked = false
                genreScience.isChecked = false
                genreBio.isChecked = false
            }
        }

        // === ІНІЦІАЛІЗАЦІЯ ФІЛЬТРІВ ===
        filterGenreSpinner = findViewById(R.id.spinner_filter_genre)
        ratingSeekBar = findViewById(R.id.seekbar_rating)
        seekbarValue = findViewById(R.id.seekbar_value)

        val genres = listOf("Усі", "Фікшн", "Наука", "Біографія")
        val genreAdapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, genres)
        genreAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        filterGenreSpinner.adapter = genreAdapter

        filterGenreSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>, view: View?, position: Int, id: Long) {
                selectedGenre = genres[position]
                applyFilters()
            }

            override fun onNothingSelected(parent: AdapterView<*>) {}
        }

        ratingSeekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                minRating = progress
                seekbarValue.text = "Оцінка: $minRating+"
                applyFilters()
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {}
            override fun onStopTrackingTouch(seekBar: SeekBar?) {}
        })
    }

    private fun applyFilters() {
        val filtered = bookList.filter { book ->
            val genreMatch = selectedGenre == "Усі" || book.genres.contains(selectedGenre)
            val ratingMatch = book.rating >= minRating
            genreMatch && ratingMatch
        }

        adapter.updateList(filtered)

    }
}
