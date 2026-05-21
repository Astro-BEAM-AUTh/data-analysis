>  **CURRENT BRANCH: `exp-ica-background-removal`** 
> 
> **Purpose of this branch:** This branch focuses on the evaluation and implementation of the **Independent Component Analysis (ICA)** algorithm for separating the true radio astronomical signal from the changing background (background drift). Unlike GPR, which operates on a single observation, ICA requires observations across different time segments and relies on signals with a non-Gaussian distribution.
>
> *(For general instructions on server deployment and the main pipeline setup, please refer to the `main` branch README).*
>
> ---

# 🧠 ICA (Independent Component Analysis) Background Removal

## 📋 Method Overview (ICA vs. ON-OFF Subtraction)
In classical radio astronomy, background removal relies on the ON-OFF calibration technique (comparing a target observation with an empty sky observation). However, simple subtraction fails when the background exhibits a temporal drift between these phases. 

The ICA approach solves this by treating it as a Blind Source Separation problem. By modeling the background variations and the spectral line as statistically independent components, the algorithm can fully isolate the background, even in the presence of strong Radio Frequency Interference (RFI).

## 📂 Branch Contents

* **`IcaTesting.ipynb`**: The main development notebook. It includes the generation of 2D synthetic data (time-frequency), the execution of the FastICA algorithm, the automated recognition of components via statistical indicators, and real-time performance evaluation.

## 🛠️ Pipeline Architecture & Processing Stages

The processing flow in this research branch is structured into the following stages:

### 1. Observation Matrix Simulation
Since ICA requires multiple samples over time, a 2D observation array (frequencies $\times$ time segments) is constructed:
* A temporal slope/drift is simulated in the background at each step to mimic real-world instability.
* An ON-OFF pattern is applied, where the spectral line is present only in half of the simulated time segments.

### 2. Independent Component Extraction (FastICA)
We utilize the `FastICA` class from `sklearn.decomposition`. The algorithm searches for linear combinations of the data that maximize non-Gaussianity, decomposing the signal mixture into its original, independent sources.

### 3. Automated Signal Recognition via Kurtosis
The components returned by ICA are not in a predefined order. For the automated recognition of the spectral line:
* The **Kurtosis** of each component is calculated using `scipy.stats.kurtosis`.
* The spectral line, being a strong mathematical anomaly, exhibits an extremely high Kurtosis value (highly non-Gaussian).
* The smooth background profile shows a much lower value, allowing the pipeline to classify and separate them automatically.

### 4. RFI Resilience Testing
A strong external interference (Strong Tip / Spike) is experimentally introduced into the signal. ICA proves its resilience by isolating this RFI into a completely separate third component, leaving the scientific observation's spectral line intact.

### 5. Reconstruction & Smoothing
After isolating the background, the **Savitzky-Golay** digital filter (`savgol_filter` from `scipy.signal`) is applied to reduce residual high-frequency noise, ensuring a clean baseline before final extraction.

## 📊 Evaluation Metrics
The algorithm's performance is measured across two axes:
1. **Normalized Root Mean Square Error (NRMSE):** To measure the accuracy of the background reconstruction compared to the Ground Truth.
2. **Execution Duration:** Recording the execution time in seconds to ensure the algorithm can meet the real-time requirements of the telescope's server processing.

## 💻 Dependencies

The following libraries are required to run the notebook locally:

```bash
pip install numpy matplotlib scikit-learn scipy
