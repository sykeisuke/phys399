#!/usr/bin/env python3
import numpy as np
import pandas as pd

def generate_data(n_signal=2000, n_bkg=50000,
                  mu=8.0, sigma=0.5, tau=3.0,
                  seed=42,
                  out_csv_labeled="sample_lec10.csv",
                  out_csv_unlabeled="sample_lec11.csv"):
    """
    Generate toy dataset with exponential background + gaussian peak (signal).
    Outputs both labeled and unlabeled CSV files.
    """

    np.random.seed(seed)

    # background: exponential
    x_bkg = np.random.exponential(scale=tau, size=n_bkg)
    y_bkg = np.zeros(n_bkg, dtype=int)  # label=0

    # signal: gaussian
    x_sig = np.random.normal(loc=mu, scale=sigma, size=n_signal)
    y_sig = np.ones(n_signal, dtype=int)  # label=1

    # combine
    x = np.concatenate([x_bkg, x_sig])
    y = np.concatenate([y_bkg, y_sig])

    # labeled dataframe
    df_labeled = pd.DataFrame({"x": x, "label": y})
    df_labeled.to_csv(out_csv_labeled, index=False)
    print(f"Labeled dataset saved to {out_csv_labeled}")

    # unlabeled dataframe (drop label column)
    df_unlabeled = pd.DataFrame({"x": x})
    df_unlabeled.to_csv(out_csv_unlabeled, index=False)
    print(f"Unlabeled dataset saved to {out_csv_unlabeled}")

    return df_labeled, df_unlabeled

if __name__ == "__main__":
    generate_data()
