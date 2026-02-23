import customtkinter as ctk
import pandas as pd
import os
from datetime import datetime, timedelta
from database.history_db import load_history

class OwnerDashboard(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.title("Owner Dashboard")
        self.geometry("500x500")

        ctk.CTkLabel(self, text="Owner Analytics", font=("Arial", 20)).pack(pady=20)

        history = load_history()
        df = pd.DataFrame(history)

        if df.empty:
            daily = weekly = monthly = yearly = 0
        else:
            df["date"] = pd.to_datetime(df["date"])
            today = datetime.now().date()

            daily = df[df["date"].dt.date == today]["total"].sum()

            weekly = df[df["date"] >= pd.Timestamp.now() - pd.Timedelta(days=7)]["total"].sum()

            monthly = df[
                (df["date"].dt.month == today.month) &
                (df["date"].dt.year == today.year)
            ]["total"].sum()

            yearly = df[df["date"].dt.year == today.year]["total"].sum()

        ctk.CTkLabel(self, text=f"Today's Sales: ₹{daily}").pack(pady=10)
        ctk.CTkLabel(self, text=f"Weekly Sales: ₹{weekly}").pack(pady=10)
        ctk.CTkLabel(self, text=f"Monthly Sales: ₹{monthly}").pack(pady=10)
        ctk.CTkLabel(self, text=f"Yearly Sales: ₹{yearly}").pack(pady=10)

        ctk.CTkButton(
            self,
            text="Open Excel Folder",
            command=self.open_excel
        ).pack(pady=30)

    def open_excel(self):
        os.startfile("sales_excel")