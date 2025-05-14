package com.example.lab3

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class BookAdapter(private var books: MutableList<Book>, private val onClick: (Book) -> Unit)
    : RecyclerView.Adapter<BookAdapter.BookViewHolder>() {

    inner class BookViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val title = itemView.findViewById<TextView>(R.id.titleTextView)
        val author = itemView.findViewById<TextView>(R.id.authorTextView)
        val rating = itemView.findViewById<TextView>(R.id.ratingTextView)
        val genres = itemView.findViewById<TextView>(R.id.genresTextView)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BookViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_book, parent, false)
        return BookViewHolder(view)
    }

    override fun getItemCount() = books.size

    override fun onBindViewHolder(holder: BookViewHolder, position: Int) {
        val book = books[position]
        holder.title.text = book.title
        holder.author.text = "Автор: ${book.author}"
        holder.rating.text = "Оцінка: ${book.rating}"
        holder.genres.text = "Жанри: ${book.genres.joinToString(", ")}"

        holder.itemView.setOnClickListener {
            onClick(book)
        }
    }

    // 🆕 Метод оновлення списку після фільтрації
    fun updateList(newList: List<Book>) {
        books = newList.toMutableList()
        notifyDataSetChanged()
    }
}
