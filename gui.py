import customtkinter
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from summarize import *


class App(customtkinter.CTk):

    def __init__(self):
        # window setup
        super().__init__()
        self.selected_pair = None
        self.title("D3D Market Scanner - v1.0")
        self.minsize(1280, 720)
        self.maxsize(1920, 1080)
        # self.iconbitmap("logo.ico")
        self._set_appearance_mode("System")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsw")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        # navigation items
        self.navigation_label = customtkinter.CTkLabel(self.navigation_frame, text="Menu", compound="left",
                                                       font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_label.grid(row=0, column=0, padx="20", pady="20", sticky="nsew")
        self.navigation_button1 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="Summary",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w", command=lambda: self.nav_button_event("Summary"))
        self.navigation_button1.grid(row=1, column=0, sticky="ew")
        self.navigation_button2 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="Major Pairs",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          command=lambda: self.nav_button_event("Major Pairs"))
        self.navigation_button2.grid(row=2, column=0, sticky="ew")
        self.navigation_button3 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="EUR & CHF Pairs",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          command=lambda: self.nav_button_event("EUR & CHF Pairs"))
        self.navigation_button3.grid(row=3, column=0, sticky="ew")
        self.navigation_button4 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="GBP & CAD Pairs",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          command=lambda: self.nav_button_event("GBP & CAD Pairs"))
        self.navigation_button4.grid(row=4, column=0, sticky="ew")
        self.navigation_button5 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="AUD & NZD Pairs",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          command=lambda: self.nav_button_event("AUD & NZD Pairs"))
        self.navigation_button5.grid(row=5, column=0, sticky="ew")
        self.navigation_appearance_button = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                        values=["System", "Dark", "Light"],
                                                                        command=self.change_appearance_mode_event)
        self.navigation_appearance_button.grid(row=10, column=0, padx=20, pady=20, sticky="s")

        # summary frame
        self.summary_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.summary_frame.grid_columnconfigure(0, weight=1)

        self.summary_frame_label = customtkinter.CTkLabel(master=self.summary_frame, text="Score Summary Heatmap",
                                                          font=customtkinter.CTkFont(size=10, weight="bold"))
        self.summary_frame_label.grid(row="0", column="0", pady="20", sticky="n")

        table_style = ttk.Style()
        table_style.configure("Treeview", rowheight=50, font=customtkinter.CTkFont(size=8))

        self.all_score_summary_tree = ttk.Treeview(self.summary_frame,
                                                   columns=(
                                                       "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"),
                                                   show='headings', height=14, selectmode="none")
        self.all_score_summary_tree.column("# 1", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 1", text="Currency")
        self.all_score_summary_tree.column("# 2", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 2", text="Interest Rate")
        self.all_score_summary_tree.column("# 3", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 3", text="GDP Growth")
        self.all_score_summary_tree.column("# 4", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 4", text="Inflation Rate")
        self.all_score_summary_tree.column("# 5", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 5", text="Unemployment Rate")
        self.all_score_summary_tree.column("# 6", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 6", text="COT Report")
        self.all_score_summary_tree.column("# 7", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 7", text="Retail Sentiment")
        self.all_score_summary_tree.column("# 8", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 8", text="Technicals")
        self.all_score_summary_tree.column("# 9", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 9", text="Seasonality")
        self.all_score_summary_tree.column("# 10", anchor="center", width=124)
        self.all_score_summary_tree.heading("# 10", text="Total")

        self.tree_scroll = ttk.Scrollbar(self.summary_frame)
        self.tree_scroll.configure(command=self.all_score_summary_tree.yview)
        self.all_score_summary_tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.grid(row=1, column=1, sticky="nse")

        self.all_score_summary_tree.grid(row=1, column=0, sticky="nsw", pady="0", padx="0")

        # pairs frame
        self.pairs_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", width=980)
        self.pairs_frame.grid_columnconfigure(0, weight=1)
        self.pairs_frame.grid(row=0, column=0, sticky="n")

        # pairs button frame
        self.pairs_button_frame = customtkinter.CTkFrame(master=self.pairs_frame, corner_radius=10)
        self.grid_columnconfigure(0, weight=1)
        self.pairs_button_frame.grid(padx="20", pady="30", sticky="n")

        # pairs button items
        self.eurusd_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="EURUSD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("EURUSD"))
        self.eurusd_button.grid(row="0", column="0")
        self.gbpusd_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="GBPUSD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("GBPUSD"))
        self.gbpusd_button.grid(row="0", column="1")
        self.audusd_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="AUDUSD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("AUDUSD"))
        self.audusd_button.grid(row="0", column="2")
        self.nzdusd_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="NZDUSD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("NZDUSD"))
        self.nzdusd_button.grid(row="0", column="3")
        self.usdcad_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="USDCAD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("USDCAD"))
        self.usdcad_button.grid(row="0", column="4")
        self.usdchf_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="USDCHF",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("USDCHF"))
        self.usdchf_button.grid(row="0", column="5", sticky="ew")
        self.usdjpy_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="USDJPY",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("USDJPY"))
        self.usdjpy_button.grid(row="0", column="6", sticky="ew")
        self.eurgbp_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="EURGBP",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("EURGBP"))
        self.eurgbp_button.grid(row="1", column="0", sticky="ew")
        self.euraud_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="EURAUD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("EURAUD"))
        self.euraud_button.grid(row="1", column="1", sticky="ew")
        self.eurnzd_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="EURNZD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("EURNZD"))
        self.eurnzd_button.grid(row="1", column="2", sticky="ew")
        self.eurcad_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="EURCAD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("EURCAD"))
        self.eurcad_button.grid(row="1", column="3", sticky="ew")
        self.eurchf_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="EURCHF",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("EURCHF"))
        self.eurchf_button.grid(row="1", column="4", sticky="ew")
        self.eurjpy_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="EURJPY",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("EURJPY"))
        self.eurjpy_button.grid(row="1", column="5", sticky="ew")
        self.chfjpy_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="CHFJPY",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("CHFJPY"))
        self.chfjpy_button.grid(row="1", column="6", sticky="ew")
        self.gbpaud_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="GBPAUD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("GBPAUD"))
        self.gbpaud_button.grid(row="2", column="0", sticky="ew")
        self.gbpnzd_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="GBPNZD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("GBPNZD"))
        self.gbpnzd_button.grid(row="2", column="1", sticky="ew")
        self.gbpcad_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="GBPCAD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("GBPCAD"))
        self.gbpcad_button.grid(row="2", column="2", sticky="ew")
        self.gbpchf_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="GBPCHF",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("GBPCHF"))
        self.gbpchf_button.grid(row="2", column="3", sticky="ew")
        self.gbpjpy_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="GBPJPY",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("GBPJPY"))
        self.gbpjpy_button.grid(row="2", column="4", sticky="ew")
        self.cadchf_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="CADCHF",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("CADCHF"))
        self.cadchf_button.grid(row="2", column="5", sticky="ew")
        self.cadjpy_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="CADJPY",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("CADJPY"))
        self.cadjpy_button.grid(row="2", column="6", sticky="ew")
        self.audnzd_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="AUDNZD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("AUDNZD"))
        self.audnzd_button.grid(row="3", column="0", sticky="ew")
        self.audcad_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="AUDCAD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("AUDCAD"))
        self.audcad_button.grid(row="3", column="1", sticky="ew")
        self.audchf_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="AUDCHF",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("AUDCHF"))
        self.audchf_button.grid(row="3", column="2", sticky="ew")
        self.audjpy_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="AUDJPY",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("AUDJPY"))
        self.audjpy_button.grid(row="3", column="3", sticky="ew")
        self.nzdcad_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="NZDCAD",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("NZDCAD"))
        self.nzdcad_button.grid(row="3", column="4", sticky="ew")
        self.nzdchf_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="NZDCHF",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("NZDCHF"))
        self.nzdchf_button.grid(row="3", column="5", sticky="ew")
        self.nzdjpy_button = customtkinter.CTkButton(master=self.pairs_button_frame, text="NZDJPY",
                                                     corner_radius=0,
                                                     height=40, border_spacing=10, fg_color="transparent",
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     command=lambda: self.pair_button_event("NZDJPY"))
        self.nzdjpy_button.grid(row="3", column="6", sticky="ew")

        # score summary frame
        self.score_summary_frame = customtkinter.CTkFrame(master=self.pairs_frame, corner_radius=10, width=980)
        self.grid_columnconfigure(10, weight=1)
        self.score_summary_frame.grid(ipady=10)

        # score summary items
        self.scores_summary_label = customtkinter.CTkLabel(master=self.score_summary_frame, text="Score summary",
                                                           compound="left",
                                                           font=customtkinter.CTkFont(size=14, weight="bold"),
                                                           width=980)
        self.scores_summary_label.grid(row="0", column="0", padx="0", pady="10")

        self.score_summary_tree = ttk.Treeview(self.score_summary_frame,
                                               columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"),
                                               show='headings', height=1, selectmode="none")
        self.score_summary_tree.column("# 1", anchor="center", width=130)
        self.score_summary_tree.heading("# 1", text="Interest Rate")
        self.score_summary_tree.column("# 2", anchor="center", width=130)
        self.score_summary_tree.heading("# 2", text="GDP Growth")
        self.score_summary_tree.column("# 3", anchor="center", width=130)
        self.score_summary_tree.heading("# 3", text="Inflation Rate")
        self.score_summary_tree.column("# 4", anchor="center", width=130)
        self.score_summary_tree.heading("# 4", text="Unemployment Rate")
        self.score_summary_tree.column("# 5", anchor="center", width=130)
        self.score_summary_tree.heading("# 5", text="COT Report")
        self.score_summary_tree.column("# 6", anchor="center", width=130)
        self.score_summary_tree.heading("# 6", text="Retail Sentiment")
        self.score_summary_tree.column("# 7", anchor="center", width=130)
        self.score_summary_tree.heading("# 7", text="Technicals")
        self.score_summary_tree.column("# 8", anchor="center", width=130)
        self.score_summary_tree.heading("# 8", text="Seasonality")
        self.score_summary_tree.column("# 9", anchor="center", width=130)
        self.score_summary_tree.heading("# 9", text="Total")

        # Insert the data in Treeview widget

        self.score_summary_tree.grid(row=2, column=0, sticky="n")

        # fundamentals frame
        self.fundamental_frame = customtkinter.CTkFrame(master=self.pairs_frame, corner_radius=10, width=600)
        self.fundamental_frame.grid(row=3, padx=18, pady=10, ipady=10, sticky="nw")

        # fundamental frame items
        self.fundamental_label = customtkinter.CTkLabel(master=self.fundamental_frame, text="Fundamentals",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=14, weight="bold"),
                                                        width=600)
        self.fundamental_label.grid(row="0", column="0", padx="0", pady="10")
        self.economic_report_label = customtkinter.CTkLabel(master=self.fundamental_frame, text="Economic Indicators")
        self.economic_report_label.grid(row="1", column="0", columnspan="3", sticky="n")
        self.fundamental_tree = ttk.Treeview(self.fundamental_frame,
                                             columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"),
                                             show='headings', height=2, selectmode="none")
        self.fundamental_tree.column("# 1", anchor="center", width=60)
        self.fundamental_tree.heading("# 1", text="Currency")
        self.fundamental_tree.column("# 2", anchor="center", width=90)
        self.fundamental_tree.heading("# 2", text="Interest R.")
        self.fundamental_tree.column("# 3", anchor="center", width=70)
        self.fundamental_tree.heading("# 3", text="↑↓")
        self.fundamental_tree.column("# 4", anchor="center", width=90)
        self.fundamental_tree.heading("# 4", text="GDP G.R.")
        self.fundamental_tree.column("# 5", anchor="center", width=70)
        self.fundamental_tree.heading("# 5", text="↑↓")
        self.fundamental_tree.column("# 6", anchor="center", width=90)
        self.fundamental_tree.heading("# 6", text="Inflation R.")
        self.fundamental_tree.column("# 7", anchor="center", width=70)
        self.fundamental_tree.heading("# 7", text="↑↓")
        self.fundamental_tree.column("# 8", anchor="center", width=115)
        self.fundamental_tree.heading("# 8", text="Unemployment R.")
        self.fundamental_tree.column("# 9", anchor="center", width=70)
        self.fundamental_tree.heading("# 9", text="↑↓")

        self.fundamental_tree.grid(row=2, column=0, sticky="n")

        # sentiments frame
        self.sentiment_frame = customtkinter.CTkFrame(master=self.pairs_frame, corner_radius=10, width=360)
        self.sentiment_frame.columnconfigure(5, weight=1)
        self.sentiment_frame.grid(row=3, padx=18, pady=10, ipady=10, sticky="ne")

        # sentiment frame items
        self.sentiment_label = customtkinter.CTkLabel(master=self.sentiment_frame, text="Sentiments",
                                                      compound="left",
                                                      font=customtkinter.CTkFont(size=14, weight="bold"),
                                                      width=360)
        self.sentiment_label.grid(row="0", column="0", columnspan=5, padx="0", pady="10")

        self.sentiment_cot_label = customtkinter.CTkLabel(master=self.sentiment_frame, text="COT Report", width=210)
        self.sentiment_cot_label.grid(row="1", column="0", columnspan="3", sticky="w")
        self.sentiment_retail_label = customtkinter.CTkLabel(master=self.sentiment_frame, text="Retail Sentiment",
                                                             width=140)
        self.sentiment_retail_label.grid(row="1", column="3", columnspan="2", sticky="w")

        self.cot_tree = ttk.Treeview(self.sentiment_frame, columns=("c1", "c2", "c3"),
                                     show='headings', height=2, selectmode="none")
        self.cot_tree.column("# 1", anchor="center", width=80)
        self.cot_tree.heading("# 1", text="Currency")
        self.cot_tree.column("# 2", anchor="center", width=80)
        self.cot_tree.heading("# 2", text="Long")
        self.cot_tree.column("# 3", anchor="center", width=80)
        self.cot_tree.heading("# 3", text="Short")

        self.cot_tree.grid(row=2, column=0, sticky="n", padx=10)

        self.retail_tree = ttk.Treeview(self.sentiment_frame, columns=("c1", "c2"),
                                        show='headings', height=1, selectmode="none")
        self.retail_tree.column("# 1", anchor="center", width=80)
        self.retail_tree.heading("# 1", text="Long")
        self.retail_tree.column("# 2", anchor="center", width=80)
        self.retail_tree.heading("# 2", text="Short")

        self.retail_tree.grid(row=2, column=3, sticky="n", padx=10)

        self.seasonality_frame = customtkinter.CTkFrame(master=self.pairs_frame, corner_radius=10, width=600)
        self.seasonality_frame.grid(row=4, padx=18, pady=0, ipady=10, sticky="nw")

        # fundamental frame items
        self.seasonality_label = customtkinter.CTkLabel(master=self.seasonality_frame, text="Seasonality Report",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=14, weight="bold"),
                                                        width=600)
        self.seasonality_label.grid(row="0", column="0", padx="0", pady="10")
        self.sub_seasonality_frame = customtkinter.CTkFrame(master=self.seasonality_frame, corner_radius=10,
                                                            fg_color="transparent")
        self.sub_seasonality_frame.grid(row=1, padx=18, pady=0, ipady=0, sticky="nw")

        self.technical_frame = customtkinter.CTkFrame(master=self.pairs_frame, corner_radius=10, width=360)
        self.technical_frame.grid(row=4, padx=18, pady=0, ipady=10, sticky="ne")

        # fundamental frame items
        self.technical_label = customtkinter.CTkLabel(master=self.technical_frame, text="Technical Indicators",
                                                      compound="left",
                                                      font=customtkinter.CTkFont(size=14, weight="bold"),
                                                      width=360)
        self.technical_label.grid(row="0", column="0", padx="0", pady="10")
        self.technical_tree = ttk.Treeview(self.technical_frame,
                                           columns=("c1", "c2", "c3", "c4"),
                                           show='headings', height=1, selectmode="none")
        self.technical_tree.column("# 1", anchor="center", width=170)
        self.technical_tree.heading("# 1", text="Overall Report")
        self.technical_tree.column("# 2", anchor="center", width=86)
        self.technical_tree.heading("# 2", text="Buy's")
        self.technical_tree.column("# 3", anchor="center", width=86)
        self.technical_tree.heading("# 3", text="Neutral's")
        self.technical_tree.column("# 4", anchor="center", width=86)
        self.technical_tree.heading("# 4", text="Sell's")

        self.technical_tree.grid(row=1, column=0, sticky="n")
        self.nav_button_event("Summary")

    # navigation button function
    def nav_button_event(self, name):
        self.navigation_button1.configure(fg_color=("gray75", "gray25") if name == "Summary" else "transparent")
        self.navigation_button2.configure(fg_color=("gray75", "gray25") if name == "Major Pairs" else "transparent")
        self.navigation_button3.configure(fg_color=("gray75", "gray25") if name == "EUR & CHF Pairs" else "transparent")
        self.navigation_button4.configure(fg_color=("gray75", "gray25") if name == "GBP & CAD Pairs" else "transparent")
        self.navigation_button5.configure(fg_color=("gray75", "gray25") if name == "AUD & NZD Pairs" else "transparent")

        # show selected frame
        if name == "Summary":
            self.summary_frame.grid(row=0, column=1, pady=20, sticky="n")
            for item in self.all_score_summary_tree.get_children():
                self.all_score_summary_tree.delete(item)
            all_summary_data = []
            for pair in all_pairs:
                all_summary_data.append(summary_table(pair, True))
            counter = 0
            for x in range(100, -101, -1):
                for data in all_summary_data:
                    if data[9] == x:
                        counter += 1
                        self.all_score_summary_tree.insert('', 'end', text=str(counter), values=data)
        else:
            self.summary_frame.grid_forget()
        if name == "Major Pairs" or name == "EUR & CHF Pairs" or name == "GBP & CAD Pairs" or name == "AUD & NZD Pairs":
            self.pairs_frame.grid(row=0, column=1, sticky="n")
        else:
            self.pairs_frame.grid_forget()
        if name == "Major Pairs":
            self.pair_button_event("EURUSD")
            self.hide_all()
            self.show_r1()
        if name == "EUR & CHF Pairs":
            self.pair_button_event("EURGBP")
            self.hide_all()
            self.show_r2()
        if name == "GBP & CAD Pairs":
            self.pair_button_event("GBPAUD")
            self.hide_all()
            self.show_r3()
        if name == "AUD & NZD Pairs":
            self.pair_button_event("AUDNZD")
            self.hide_all()
            self.show_r4()

    def show_r1(self):
        self.eurusd_button.grid(row="0", column="0")
        self.gbpusd_button.grid(row="0", column="1")
        self.audusd_button.grid(row="0", column="2")
        self.nzdusd_button.grid(row="0", column="3")
        self.usdcad_button.grid(row="0", column="4")
        self.usdchf_button.grid(row="0", column="5")
        self.usdjpy_button.grid(row="0", column="6")

    def show_r2(self):
        self.eurgbp_button.grid(row="1", column="0")
        self.euraud_button.grid(row="1", column="1")
        self.eurnzd_button.grid(row="1", column="2")
        self.eurcad_button.grid(row="1", column="3")
        self.eurchf_button.grid(row="1", column="4")
        self.eurjpy_button.grid(row="1", column="5")
        self.chfjpy_button.grid(row="1", column="6")

    def show_r3(self):
        self.gbpaud_button.grid(row="2", column="0")
        self.gbpnzd_button.grid(row="2", column="1")
        self.gbpcad_button.grid(row="2", column="2")
        self.gbpchf_button.grid(row="2", column="3")
        self.gbpjpy_button.grid(row="2", column="4")
        self.cadchf_button.grid(row="2", column="5")
        self.cadjpy_button.grid(row="2", column="6")

    def show_r4(self):
        self.audnzd_button.grid(row="3", column="0")
        self.audcad_button.grid(row="3", column="1")
        self.audchf_button.grid(row="3", column="2")
        self.audjpy_button.grid(row="3", column="3")
        self.nzdcad_button.grid(row="3", column="4")
        self.nzdchf_button.grid(row="3", column="5")
        self.nzdjpy_button.grid(row="3", column="6")

    def hide_all(self):
        self.eurusd_button.grid_forget()
        self.gbpusd_button.grid_forget()
        self.audusd_button.grid_forget()
        self.nzdusd_button.grid_forget()
        self.usdcad_button.grid_forget()
        self.usdchf_button.grid_forget()
        self.usdjpy_button.grid_forget()
        self.eurgbp_button.grid_forget()
        self.euraud_button.grid_forget()
        self.eurnzd_button.grid_forget()
        self.eurcad_button.grid_forget()
        self.eurchf_button.grid_forget()
        self.eurjpy_button.grid_forget()
        self.chfjpy_button.grid_forget()
        self.gbpaud_button.grid_forget()
        self.gbpnzd_button.grid_forget()
        self.gbpcad_button.grid_forget()
        self.gbpchf_button.grid_forget()
        self.gbpjpy_button.grid_forget()
        self.cadchf_button.grid_forget()
        self.cadjpy_button.grid_forget()
        self.audnzd_button.grid_forget()
        self.audcad_button.grid_forget()
        self.audchf_button.grid_forget()
        self.audjpy_button.grid_forget()
        self.nzdcad_button.grid_forget()
        self.nzdchf_button.grid_forget()
        self.nzdjpy_button.grid_forget()

    # appearance button function
    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # pair button function
    def pair_button_event(self, name):
        # set button color for selected button

        self.eurusd_button.configure(fg_color=("gray75", "gray25") if name == "EURUSD" else "transparent")
        self.gbpusd_button.configure(fg_color=("gray75", "gray25") if name == "GBPUSD" else "transparent")
        self.audusd_button.configure(fg_color=("gray75", "gray25") if name == "AUDUSD" else "transparent")
        self.nzdusd_button.configure(fg_color=("gray75", "gray25") if name == "NZDUSD" else "transparent")
        self.usdcad_button.configure(fg_color=("gray75", "gray25") if name == "USDCAD" else "transparent")
        self.usdchf_button.configure(fg_color=("gray75", "gray25") if name == "USDCHF" else "transparent")
        self.usdjpy_button.configure(fg_color=("gray75", "gray25") if name == "USDJPY" else "transparent")

        self.eurgbp_button.configure(fg_color=("gray75", "gray25") if name == "EURGBP" else "transparent")
        self.euraud_button.configure(fg_color=("gray75", "gray25") if name == "EURAUD" else "transparent")
        self.eurnzd_button.configure(fg_color=("gray75", "gray25") if name == "EURNZD" else "transparent")
        self.eurcad_button.configure(fg_color=("gray75", "gray25") if name == "EURCAD" else "transparent")
        self.eurchf_button.configure(fg_color=("gray75", "gray25") if name == "EURCHF" else "transparent")
        self.eurjpy_button.configure(fg_color=("gray75", "gray25") if name == "EURJPY" else "transparent")
        self.chfjpy_button.configure(fg_color=("gray75", "gray25") if name == "CHFJPY" else "transparent")

        self.gbpaud_button.configure(fg_color=("gray75", "gray25") if name == "GBPAUD" else "transparent")
        self.gbpnzd_button.configure(fg_color=("gray75", "gray25") if name == "GBPNZD" else "transparent")
        self.gbpcad_button.configure(fg_color=("gray75", "gray25") if name == "GBPCAD" else "transparent")
        self.gbpchf_button.configure(fg_color=("gray75", "gray25") if name == "GBPCHF" else "transparent")
        self.gbpjpy_button.configure(fg_color=("gray75", "gray25") if name == "GBPJPY" else "transparent")
        self.cadchf_button.configure(fg_color=("gray75", "gray25") if name == "CADCHF" else "transparent")
        self.cadjpy_button.configure(fg_color=("gray75", "gray25") if name == "CADJPY" else "transparent")

        self.audnzd_button.configure(fg_color=("gray75", "gray25") if name == "AUDNZD" else "transparent")
        self.audcad_button.configure(fg_color=("gray75", "gray25") if name == "AUDCAD" else "transparent")
        self.audchf_button.configure(fg_color=("gray75", "gray25") if name == "AUDCHF" else "transparent")
        self.audjpy_button.configure(fg_color=("gray75", "gray25") if name == "AUDJPY" else "transparent")
        self.nzdcad_button.configure(fg_color=("gray75", "gray25") if name == "NZDCAD" else "transparent")
        self.nzdchf_button.configure(fg_color=("gray75", "gray25") if name == "NZDCHF" else "transparent")
        self.nzdjpy_button.configure(fg_color=("gray75", "gray25") if name == "NZDJPY" else "transparent")

        self.selected_pair = name
        for widgets in self.sub_seasonality_frame.winfo_children():
            widgets.destroy()
        get_seasonality_data(self.selected_pair)

        yr10 = []
        yr05 = []
        yr01 = []
        for x in seasonality_data[name].keys():
            yr10.append(seasonality_data[name][x]["10-years"])
            yr05.append(seasonality_data[name][x]["5-years"])
            try:
                yr01.append(seasonality_data[name][x]["this-year"])
            except KeyError:
                pass
        try:
            fig, ax = plt.subplots(figsize=(7, 3), dpi=100)
            ax.plot(yr10, color='red', label='Last 10 Years')
            ax.plot(yr05, color='blue', label='Last 5 Years')
            ax.plot(yr01, color='black', label='This Years')
            ax.legend(loc='upper left')

            ax.set_xticklabels(['', 'Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'])
            plt.grid()
            canv = FigureCanvasTkAgg(fig, master=self.sub_seasonality_frame)
            canv.draw()

            get_widz = canv.get_tk_widget()
            get_widz.grid()
        except:
            pass

        for item in self.score_summary_tree.get_children():
            self.score_summary_tree.delete(item)
        self.score_summary_tree.insert('', 'end', text="1", values=summary_table(name, False))
        for item in self.fundamental_tree.get_children():
            self.fundamental_tree.delete(item)
        self.fundamental_tree.insert('', 'end', text="1", values=fundamental_table(name[:3]))
        self.fundamental_tree.insert('', 'end', text="2", values=fundamental_table(name[3:]))
        for item in self.cot_tree.get_children():
            self.cot_tree.delete(item)
        self.cot_tree.insert('', 'end', text="1", values=cot_table(name[:3]))
        self.cot_tree.insert('', 'end', text="2", values=cot_table(name[3:]))
        for item in self.retail_tree.get_children():
            self.retail_tree.delete(item)
        self.retail_tree.insert('', 'end', text="1", values=retail_table(name))
        for item in self.technical_tree.get_children():
            self.technical_tree.delete(item)
        self.technical_tree.insert('', 'end', text="1", values=technical_table(name))
