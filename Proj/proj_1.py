import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Nsig, Nbkg = 500, 10000

# Signal (Higgs)
m4l_sig = np.random.normal(125, 2, Nsig)
pT_max_sig = np.random.normal(45, 10, Nsig)       
eta_diff_sig = np.random.normal(0.5, 0.2, Nsig)  

# Background (ZZ*)
m4l_bkg1 = np.random.normal(90, 10, Nbkg//2)
m4l_bkg2 = np.random.exponential(30, Nbkg//2) + 100
m4l_bkg  = np.concatenate([m4l_bkg1, m4l_bkg2])

pT_max_bkg = np.random.normal(30, 12, Nbkg)      
eta_diff_bkg = np.random.normal(1.5, 0.5, Nbkg) 

df_sig = pd.DataFrame({
    "label": "signal",
    "m4l": m4l_sig,
    "pT_max": pT_max_sig,
    "eta_diff": eta_diff_sig
})

df_bkg = pd.DataFrame({
    "label": "background",
    "m4l": m4l_bkg,
    "pT_max": pT_max_bkg,
    "eta_diff": eta_diff_bkg
})

df = pd.concat([df_sig, df_bkg])
df.to_csv("proj_hzz.csv", index=False)
print(df.head())

def make_bins(x_sig, x_bkg, bin_width=None, nbins=40):
    data = np.r_[x_sig, x_bkg]
    lo, hi = data.min(), data.max()
    if bin_width is not None:
        lo = np.floor(lo/bin_width) * bin_width
        hi = np.ceil(hi/bin_width) * bin_width
        bins = np.arange(lo, hi + bin_width, bin_width)
    else:
        bins = np.linspace(lo, hi, nbins + 1)
    return bins

sig = df[df["label"] == "signal"]
bkg = df[df["label"] == "background"]

plt.figure(figsize=(15,4))

for i, (var, xlabel) in enumerate([
    ("m4l", "m4l [GeV]"),
    ("pT_max", "Max pT [GeV]"),
    ("eta_diff", "|Δη|"),
], 1):
    plt.subplot(1, 3, i)

    if var == "m4l":
        bins = make_bins(sig[var], bkg[var], bin_width=4.0)   
    elif var == "pT_max":
        bins = make_bins(sig[var], bkg[var], bin_width=2.0) 
    else:  # eta_diff
        bins = make_bins(sig[var], bkg[var], bin_width=0.1)

    plt.hist(bkg[var], bins=bins, alpha=0.5, color="steelblue", label="Background")
    plt.hist(sig[var], bins=bins, alpha=0.5, color="tomato",    label="Signal")

    plt.xlabel(xlabel); plt.ylabel("Events"); plt.title(f"{xlabel} Distribution")
    if i == 1: plt.legend()

plt.tight_layout(); plt.show()
