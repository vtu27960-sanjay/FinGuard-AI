import React from "react";

function DashboardCards() {

    return (

        <div className="row mt-4">

            <div className="col-md-3">
                <div className="card bg-primary text-white p-3">
                    <h5>Total Transactions</h5>
                    <h2>152</h2>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card bg-danger text-white p-3">
                    <h5>Fraud Detected</h5>
                    <h2>18</h2>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card bg-success text-white p-3">
                    <h5>Safe Transactions</h5>
                    <h2>134</h2>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card bg-warning text-dark p-3">
                    <h5>Model Accuracy</h5>
                    <h2>99%</h2>
                </div>
            </div>

        </div>

    );

}

export default DashboardCards;