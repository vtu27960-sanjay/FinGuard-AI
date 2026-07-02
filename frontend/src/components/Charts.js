import React from "react";
import {
    Chart as ChartJS,
    ArcElement,
    Tooltip,
    Legend,
    CategoryScale,
    LinearScale,
    BarElement
} from "chart.js";

import { Pie, Bar } from "react-chartjs-2";

ChartJS.register(
    ArcElement,
    Tooltip,
    Legend,
    CategoryScale,
    LinearScale,
    BarElement
);

function Charts() {
    const pieData = {
        labels: ["Safe", "Fraud"],
        datasets: [
            {
                data: [134, 18]
            }
        ]
    };

    const barData = {
        labels: ["Food", "Travel", "Shopping", "Electronics"],
        datasets: [
            {
                label: "Transactions",
                data: [45, 20, 35, 52]
            }
        ]
    };

    return (
        <div className="row mt-4">

            <div className="col-md-6">
                <div className="card p-3">
                    <h4>Fraud Distribution</h4>
                    <Pie data={pieData} />
                </div>
            </div>

            <div className="col-md-6">
                <div className="card p-3">
                    <h4>Transactions by Category</h4>
                    <Bar data={barData} />
                </div>
            </div>

        </div>
    );
}

export default Charts;