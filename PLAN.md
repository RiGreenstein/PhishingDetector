PROJECT TITLE 

Do Old Phishing URL Detectors Still Work Today?


MAIN RESEARCH QUESTION

How well does a phishing URL classifier trained on data from 2014
detect modern phishing URLs, and how often does it incorrectly flag
modern legitimate URLs?


WHAT THIS MEANS

I will train machine-learning models on a dataset of phishing and
legitimate URLs from 2014. Then I will test those models on a
separate, recent dataset.

The models will analyze URL text only. They will not visit websites
or inspect page content.

For example, the model might learn from patterns such as:

- URL length
- Number of dots or hyphens
- Presence of an IP address in place of a domain
- Character combinations and words in the URL

The goal is not to build a perfect phishing detector. The goal is to
investigate whether models that perform well on old data still
perform well on newer data.


RESEARCH QUESTIONS

RQ1: How well do models perform on held-out URLs from the 2014 dataset?

RQ2: How well do the same models perform on modern phishing and
legitimate URLs?

RQ3: How does performance change when test domains are different
from training domains?

OPTIONAL RQ4: How sensitive are the models to small changes in URL
formatting?


IMPORTANT LIMITATION

If performance drops on modern data, I cannot immediately say that
time alone caused the drop.

The old and modern datasets may come from different sources or use
different methods to collect and label URLs. The change could be
caused by time, data-source differences, or both.

I will discuss this limitation in my final write-up.


DATA SOURCES

1. OLD DATA: PHISHSTORM

Source:
https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset/

Download:
urlset.csv.zip

Description:
- Dataset associated with a 2014 paper.
- 48,009 phishing URLs.
- 48,009 legitimate URLs.
- The column named "domain" contains the URL text.
- The "label" column uses 1 for phishing and 0 for legitimate.

Important:
I will call this a 2014 dataset, but I will not invent an exact
collection date for each individual URL.

Backup download:
https://www.kaggle.com/datasets/joebeachcapital/phishing-urls


2. MODERN DATA: 2026 ZENODO DATASET

Source:
https://zenodo.org/records/23477065

The dataset description reports:
- 31,641 phishing URLs.
- 28,359 legitimate URLs.
- Phishing data from PhishTank and legitimate data from Tranco.

Important:
- The archive is large because it also contains screenshots.
- I only need the URL data for this project.
- I need to check the downloaded files to confirm that they include
  raw URLs and usable labels.
- Publication in 2026 does not prove that every URL was collected
  in 2026. I need to check the documentation for collection dates.

If the raw URLs or dates are unclear, I will describe the uncertainty
and look for another modern dataset.


3. OPTIONAL ADDITIONAL MODERN PHISHING DATA: OPENPHISH

Source:
https://github.com/openphish/public_feed

OpenPhish publishes a free phishing URL feed that updates every
12 hours. I can download a snapshot immediately; I do not have to
wait weeks to collect data.

Important:
- The feed contains phishing URLs, not a complete benign test set.
- I should record the date I downloaded each snapshot.
- Appearing in a snapshot does not necessarily mean the URL was first
  created or discovered on that date.
- I should check OpenPhish's terms before storing or sharing its data.
- I will not upload raw phishing URLs to a public repository.


SAFETY RULES

- Never click or visit the phishing URLs.
- Analyze the URL strings only.
- Keep raw datasets out of the public GitHub repository.
- Review dataset licenses and cite all sources.
- Do not use the model to make real-world security decisions.


PYTHON TOOLS

Core:
- Python
- pandas: loading and organizing data
- scikit-learn: models, splits, and evaluation
- matplotlib or seaborn: graphs
- tldextract: extracting registered domains
- pytest: testing data-processing functions

Optional:
- Streamlit: interactive demo
- Jupyter notebooks: exploration

I do not need deep learning or a GPU for the main project.


WHAT I WILL MEASURE

1. PHISHING RECALL
   Out of all phishing URLs, how many did the model catch?

2. FALSE POSITIVE RATE
   Out of all legitimate URLs, how many did the model incorrectly
   label as phishing?

3. PRECISION
   Out of all URLs the model flagged as phishing, how many were
   actually phishing?

4. F1 SCORE
   A combined measure of precision and recall.

5. CONFUSION MATRIX
   A table showing correct and incorrect predictions for each class.

I will also report the number of phishing and legitimate URLs in each
test set. Accuracy alone can be misleading, especially when a dataset
has many more URLs from one class than the other.


8-WEEK DAY-BY-DAY PLAN

This plan assumes roughly 1-2 hours per school day. Some days may take
longer, and catch-up days can absorb extra work.


WEEK 1: SETUP AND DATA

Day 1: Define the project.
- Create a project folder and Python virtual environment.
- Write the main research question in a README or research document.
- Record why I chose this question.
- Create a research log to track decisions and problems.

Done when:
I can explain the project in two or three sentences.

Day 2: Download the old data.
- Download PhishStorm and extract urlset.csv.
- Load it with pandas.
- Check the column names, number of rows, and label counts.
- Read the dataset description and record its citation.

Done when:
I can identify the URL and label columns and know the class counts.

Day 3: Download modern data.
- Open the Zenodo dataset page.
- Review its documentation and license.
- Download the archive if practical.
- Locate the file containing URL text and labels.
- Record the dataset version and available collection dates.

Done when:
I know whether the dataset can serve as my modern test set.

Day 4: Check the modern dataset.
- Load a small portion first.
- Identify the URL and label columns.
- Check class counts and missing values.
- Check whether dates apply to individual URLs or only the dataset.
- If raw URLs are unavailable, find a replacement instead of guessing.

Done when:
I have a usable modern dataset or a clear list of what is missing.

Day 5: Organize the data.
- Create separate folders for raw and processed data.
- Keep raw data out of GitHub.
- Make a table recording each dataset's source, date information,
  size, labels, license, and known limitations.
- Optionally download and date an OpenPhish snapshot for a second
  phishing-only evaluation.

Done when:
I can clearly explain where each dataset came from.


WEEK 2: CLEANING AND EXPLORATION

Day 6: Create a consistent format.
- Convert each dataset to common columns:
  url, label, source, and date information where available.
- Preserve the original URL strings.
- Record every transformation I apply.

Done when:
Both datasets use consistent label meanings: 1 = phishing,
0 = legitimate.

Day 7: Check data quality.
- Count missing and duplicate URLs.
- Identify exact URLs that appear in both datasets.
- Check for conflicting labels.
- Investigate problems before deciding how to handle them.

Done when:
I have a short data-quality summary.

Day 8: Explore basic differences.
- Compare URL length distributions by class and dataset.
- Compare how often URLs contain paths or schemes such as https.
- Compare the number of dots and hyphens.
- Save graphs.

Done when:
I have at least three useful visualizations.

Day 9: Investigate possible shortcuts.
- Check whether differences between phishing and legitimate URLs
  could let a model exploit dataset formatting instead of learning
  meaningful patterns.
- For example: are legitimate URLs mostly bare domains while
  phishing URLs mostly include long paths?

Done when:
I have written down potential sources of bias.

Day 10: Set up evaluation splits.
- Make a random, stratified split of the 2014 data.
- Make a second split where registered domains do not overlap
  between training and test sets.
- Extract registered domains consistently.
- Set aside the modern data as a final test set.

Done when:
I can verify that the domain-disjoint split has no shared domains.


WEEK 3: FIRST MODELS

Day 11: Learn the baseline workflow.
- Review how training and test data work in scikit-learn.
- Build a very simple baseline using a few URL features, such as
  length and dot count.

Done when:
The model trains and produces predictions on held-out 2014 data.

Day 12: Add evaluation metrics.
- Calculate recall, false positive rate, precision, and F1.
- Make a confusion matrix.
- Include test-set class counts.

Done when:
I can explain what each metric means in plain language.

Day 13: Build a character-based model.
- Use character n-gram TF-IDF with logistic regression.
- Put preprocessing and the model in a scikit-learn pipeline.
- Fit the vectorizer using training data only.

Done when:
I have a second model evaluated on the same held-out 2014 split.

Day 14: Compare random and domain-disjoint splits.
- Train and evaluate each model under both split strategies.
- Record results in a table.
- Keep the modern data untouched.

Done when:
I can explain whether the split strategy affects performance.

Day 15: Review the pipeline.
- Test that no test data is used to fit preprocessing or models.
- Check that domain groups do not overlap in the domain split.
- Repeat experiments using fixed random seeds.
- Document any problems.

Done when:
Another person could understand and reproduce my evaluation steps.


WEEK 4: MODERN-DATA EVALUATION

Day 16: Freeze my modeling choices.
- Choose which models and settings to compare.
- Record the choices before evaluating the modern test set.
- Do not tune the model on the final modern test set.

Done when:
I have a written plan for the comparison.

Day 17: Evaluate on modern data.
- Apply the same trained 2014 models to the modern URLs.
- Calculate the same metrics used for the old test data.
- Record the sample counts.

Done when:
I have the first old-versus-modern results table.

Day 18: Check for overlap.
- Compare exact URLs between old training and modern test data.
- Report any overlap.
- Run a separate evaluation excluding overlapping URLs.
- Also examine whether registered domains overlap.

Done when:
I can explain how overlap might affect the results.

Day 19: Analyze the errors.
- Examine URL characteristics of false positives and false negatives
  without visiting the URLs.
- Look for recurring patterns, such as long paths or unusual domains.
- Avoid claiming a pattern is universal based on a few examples.

Done when:
I have a short list of observed error patterns.

Day 20: Make graphs.
- Plot phishing recall on old and modern test sets.
- Plot false positive rates on old and modern test sets.
- Label sample sizes and dataset sources.

Done when:
The comparison is understandable without reading the code.


WEEK 5: STRENGTHEN THE EVIDENCE

Day 21: Investigate source bias.
- Compare the structure and collection methods of both datasets.
- Check whether one class has formatting differences tied to its source.
- Write down plausible alternative explanations for any performance drop.

Done when:
I have a limitations list.

Day 22: Test a simple shortcut model.
- Train a model using only basic features such as URL length and
  whether a path exists.
- Compare it with the character-based model.

Done when:
I know whether simple formatting alone predicts labels unusually well.

Day 23: Examine performance by subgroup.
- Compare results for URLs with and without paths.
- If enough examples exist, compare short and long URLs.
- Report subgroup sizes so small groups are not overinterpreted.

Done when:
I have one or two useful subgroup tables.

Day 24: Estimate uncertainty.
- Learn how to calculate confidence intervals, for example by
  bootstrapping test examples.
- Clearly state the method and its assumptions.
- If many URLs share domains, note that they are not fully independent.

Done when:
The main results include uncertainty estimates or a clear explanation
of why they do not.

Day 25: Write preliminary findings.
- Summarize what happened on old data.
- Summarize what happened on modern data.
- State what I can and cannot conclude.

Done when:
I have a one-page results draft.


WEEK 6: OPTIONAL ROBUSTNESS EXTENSION

Only start this week if the main comparison is working.

Day 26: Define the robustness question.
- Ask whether the model gives consistent predictions for carefully
  selected equivalent URL representations.
- Document what each transformation changes and why it should or
  should not preserve the destination.

Done when:
I have precise rules for the test.

Day 27: Create a small test set.
- Select a held-out sample of URLs.
- Apply only transformations whose behavior I understand.
- Keep original and transformed URLs paired.
- Do not visit the URLs.

Done when:
I have documented pairs for testing.

Day 28: Measure prediction changes.
- Compare each original URL's prediction with its transformed version.
- Count prediction flips and changes in model scores.
- Report results separately for phishing and legitimate URLs.

Done when:
I have a table of consistency results.

Day 29: Check validity and limitations.
- Explain that changing a domain, adding a subdomain, or changing a
  path can lead to a different or nonexistent resource.
- Do not claim such changes preserve the original website.
- Do not claim an edited URL is a functioning phishing page without
  independent evidence.

Done when:
Every transformation has a clear validity note.

Day 30: Summarize the extension.
- Identify which representation changes affected predictions.
- State what the test shows and does not show.

Done when:
I have a short robustness section for the write-up.

If I skip this extension, I will use Week 6 to improve the main
analysis and documentation.


WEEK 7: WRITE-UP AND REPRODUCIBILITY

Day 31: Organize the repository.
- Separate reusable Python scripts from notebooks.
- Add a .gitignore so raw data is not published.
- Add a requirements file.

Done when:
The repository is understandable and does not expose raw phishing data.

Day 32: Document how to run the project.
- Explain where each dataset must be downloaded.
- Document preprocessing, training, and evaluation steps.
- Record versions, random seeds, and dataset versions.

Done when:
Someone with the datasets could follow the instructions.

Day 33: Draft the methods section.
- Explain datasets, labels, cleaning, splits, models, and metrics.
- Explain how I avoided leakage.

Done when:
The experiment could be understood without seeing the code.

Day 34: Draft the results section.
- Include the main comparison table and graphs.
- Include sample sizes and uncertainty where available.
- Describe results without exaggerating.

Done when:
The reader can see what the experiment actually found.

Day 35: Draft the limitations and conclusion.
- Discuss source differences, dates, label quality, domain overlap,
  class balance, and the URL-only approach.
- Explain what I would improve with more time.

Done when:
The conclusion matches the evidence.


WEEK 8: PORTFOLIO POLISH

Day 36: Create a project summary.
- Write a clear README with the question, approach, key results,
  graphs, and limitations.
- Explain the project for someone who is not a security researcher.

Done when:
A recruiter can understand the project in a few minutes.

Day 37: Make an optional demo.
- If time allows, create a small Streamlit app that demonstrates
  model scores on user-provided URL text.
- Clearly label it as a research demonstration, not a security tool.
- Do not display or publish collected phishing URLs.

Done when:
The demo runs locally and includes a warning about its limitations.

Day 38: Reproduce the main results.
- Run the documented steps again.
- Confirm that results match or explain expected variation.
- Fix broken instructions.

Done when:
The main tables and graphs can be recreated.

Day 39: Get feedback.
- Ask a teacher, mentor, or friend to read the README.
- Ask them to explain the question and main result back to me.
- Clarify anything confusing.

Done when:
The project makes sense to someone else.

Day 40: Publish the portfolio.
- Publish the code and documentation to GitHub.
- Keep raw phishing datasets private and respect their licenses.
- Optionally record a short walkthrough.
- Write a resume bullet based on the actual results, not a prediction.

Done when:
The project has a clear question, reproducible code, results, and
an honest discussion of limitations.


FINAL DELIVERABLES

- A Python project with reusable training and evaluation code.
- A GitHub README explaining the research and findings.
- A comparison table for 2014 and modern data.
- Graphs of phishing recall and false positive rate.
- A short write-up covering methods, results, and limitations.
- Optional: a robustness experiment and Streamlit demonstration.


POTENTIAL RESUME DESCRIPTION

Built and evaluated Python phishing URL classifiers trained on a
2014 dataset; compared performance on historical and modern URLs,
analyzed false positives, and documented dataset and domain-split
biases.

I will adjust this description to match what I actually complete.
