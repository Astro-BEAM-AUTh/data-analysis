>  **CURRENT BRANCH: `exp-gpr-background-removal`** 
> 
> **Purpose of this branch:** This branch focuses on the research and evaluation of the **Gaussian Process Regression (GPR)** algorithm for background removal in radio astronomical observations. It includes the development of methods for spectral line masking, hyperparameter estimation, and baseline correction.
>
> *(For general instructions on server deployment and pipeline setup, please refer to the `main` branch README).*
>
> ---

# 🧠 GPR Background Removal Research

Unlike traditional fitting methods (such as polynomials), **GPR** acts as an "intelligent" interpolation method based on Bayesian probability. By defining a kernel as a-priori knowledge (e.g., expecting a smooth signal), GPR calculates the most probable function (posterior) that fits the data, providing not just a "best fit" line but a complete probability distribution.

## 📂 Branch Contents (Jupyter Notebooks)

The research in this branch is divided into the following core notebooks:

1. **`GPR_TestingWithMask.ipynb`**: The main and most comprehensive notebook. It implements the entire pipeline: from generating a synthetic radio astronomical signal (background + spectral line + noise), to utilizing Adaptive Masking, applying GPR, and performing the final baseline correction.
2. **`GPR_Hyperparameters.ipynb`**: Focuses exclusively on the optimal calculation of the initial hyperparameters that will feed the GPR (Noise variance, Signal variance, Length scale), utilizing Variance Decomposition and Autocorrelation techniques.
3. **`GPR_Testing.ipynb`**: Basic testing of the GPR algorithm's fitting capabilities and error evaluation.

## 🛠️ Core Methodology & Algorithms (Pipeline)

The background removal process is implemented through a series of specialized steps:

### 1. Hyperparameter Estimation
To prevent the algorithm from overfitting and to ensure fast convergence, we estimate the following in advance:
* **Noise STD:** Estimated via the median of absolute differences.
* **Signal Variance:** Calculated through variance analysis (Total Variance - Noise Variance).
* **Length Scale:** Utilizing a Gaussian Filter and Autocorrelation to find the signal's correlation length.

### 2. Spectral Line Masking
Simply applying GPR is not enough. We must "hide" the spectral line from the algorithm using:
* **Rolling Median + MAD:** Calculating a rolling median (window=1MHz) to find the background trend and estimating the noise via MAD (Median Absolute Deviation). Masking is applied where $|Data - Median| > Threshold \times \sigma_{MAD}$.
* **Size Filtering (Morphological Cleaning):** Cleaning the mask from random noise spikes (keeping only clusters that exceed a certain size threshold).
* **Edge Contamination Effect Fix:** Careful dilation (padding) of the mask to prevent the GPR from "seeing" the wings of the spectral line, which would otherwise create artificial bumps.

### 3. GPR Implementation & Kernels
Combining two `scikit-learn` Kernels:
* **RBF Kernel:** To fit the smooth background profile.
* **WhiteKernel:** To incorporate the noise level into the estimation.

### 4. Baseline Correction (Residual Detrending)
GPR often introduces a systematic vertical shift error (Floating Baseline artifact). To correct this:
* We use **Morphological Wing Detection** to isolate regions that are purely noise immediately adjacent to the spectral line.
* We perform a linear fit (Least Squares Fit) on these samples to bring the noise floor exactly back to zero (Zero Error Line).

### 5. Gaussian Fitting
The final step involves fitting a Normal Distribution (Gaussian curve) over the extracted spectral line (Ground Truth vs. Extracted) and calculating the error metrics (RMSE, $R^2$ Score).

## 💻 Dependencies

To run these notebooks locally in a development environment, the following packages are required (versions used during research are shown below):

```bash
pip install matplotlib==3.9.2 numpy==2.1.3 scikit-learn==1.7.2 scipy==1.14.1 pandas==2.2.3 seaborn==0.13.2 tqdm==4.67.1
