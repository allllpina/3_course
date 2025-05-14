package com.example.lab3

import android.app.Dialog
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AlertDialog
import androidx.fragment.app.DialogFragment

class BookDialogFragment(private val book: Book) : DialogFragment() {

    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
        val view = requireActivity().layoutInflater.inflate(R.layout.dialog_book, null)

        val titleText = view.findViewById<TextView>(R.id.dialogTitle)
        val reviewText = view.findViewById<TextView>(R.id.dialogReview)

        titleText.text = "${book.title} (${book.rating}⭐)"
        reviewText.text = book.review

        return AlertDialog.Builder(requireContext())
            .setView(view)
            .setPositiveButton("ОК", null)
            .create()
    }
}
