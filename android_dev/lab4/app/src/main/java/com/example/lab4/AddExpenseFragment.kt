package com.example.lab4

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.Toast


import androidx.navigation.fragment.findNavController
import com.example.lab4.databinding.FragmentAddExpenseBinding

// AddExpenseFragment.kt
class AddExpenseFragment : Fragment(R.layout.fragment_add_expense) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val editText = view.findViewById<EditText>(R.id.editText_expense)
        val button = view.findViewById<Button>(R.id.button_go_to_history)

        button.setOnClickListener {
            val input = editText.text.toString()
            if (input.isNotBlank()) {
                val expense = input.toFloatOrNull() ?: 0f
                val action = AddExpenseFragmentDirections
                    .actionAddExpenseFragmentToHistoryFragment(expense)
                findNavController().navigate(action)
            } else {
                Toast.makeText(requireContext(), "Enter a valid expense", Toast.LENGTH_SHORT).show()
            }
        }
    }
}


