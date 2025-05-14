package com.example.lab4

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.fragment.app.activityViewModels
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.navigation.fragment.navArgs

class HistoryFragment : Fragment(R.layout.fragment_history) {

    private val args: HistoryFragmentArgs by navArgs()
    private val viewModel: ExpenseViewModel by activityViewModels()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Перевіряємо, чи не була вже додана витрата
        if (args.expenseAmount != null) {
            viewModel.addExpense(args.expenseAmount)
        }

        // Отримуємо RecyclerView
        val recyclerView = view.findViewById<RecyclerView>(R.id.recyclerView_expenses)
        recyclerView.layoutManager = LinearLayoutManager(requireContext())
        recyclerView.adapter = ExpenseAdapter(viewModel.expenses)
    }
}
