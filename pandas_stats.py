{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "23965b23-670c-4ce4-a5a6-265c8a7c6b3a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name '_name_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 57\u001b[0m\n\u001b[1;32m     54\u001b[0m     \u001b[38;5;28;01mfor\u001b[39;00m name, path \u001b[38;5;129;01min\u001b[39;00m DATASETS\u001b[38;5;241m.\u001b[39mitems():\n\u001b[1;32m     55\u001b[0m         process_file(name, path)\n\u001b[0;32m---> 57\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43m_name_\u001b[49m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m_main_\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m     58\u001b[0m     main()\n",
      "\u001b[0;31mNameError\u001b[0m: name '_name_' is not defined"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "DATASETS = {\n",
    "    \"fb_ads\": \"2024_fb_ads_president_scored_anon.csv\",\n",
    "    \"fb_posts\": \"2024_fb_posts_president_scored_anon.csv\",\n",
    "    \"tw_posts\": \"2024_tw_posts_president_scored_anon.csv\"\n",
    "}\n",
    "\n",
    "def summarize_dataframe(df):\n",
    "    print(\"\\n--- Numeric Summary ---\")\n",
    "    print(df.describe(include='number').T)\n",
    "\n",
    "    print(\"\\n--- Categorical Summary ---\")\n",
    "    for col in df.select_dtypes(include='object').columns:\n",
    "        print(f\"{col}:\")\n",
    "        print(f\"  Unique: {df[col].nunique()}\")\n",
    "        if not df[col].value_counts().empty:\n",
    "            print(f\"  Most frequent: {df[col].value_counts().idxmax()}\")\n",
    "\n",
    "def summarize_by_group(df, group_cols):\n",
    "    print(f\"\\n--- Summary grouped by {group_cols} ---\")\n",
    "\n",
    "    # Select only numeric columns for aggregation\n",
    "    numeric_cols = df.select_dtypes(include='number').columns\n",
    "    if len(numeric_cols) == 0:\n",
    "        print(\"No numeric columns to aggregate.\")\n",
    "        return\n",
    "\n",
    "    grouped = df.groupby(group_cols)[numeric_cols].agg(['count', 'mean', 'min', 'max', 'std'])\n",
    "    print(grouped.head(3))  # Show sample of grouped stats\n",
    "\n",
    "def process_file(label, filepath):\n",
    "    print(f\"\\n========== {label.upper()} ==========\")\n",
    "    if not os.path.exists(filepath):\n",
    "        print(f\"File not found: {filepath}\")\n",
    "        return\n",
    "\n",
    "    try:\n",
    "        df = pd.read_csv(filepath)\n",
    "    except Exception as e:\n",
    "        print(f\"Failed to load {filepath}: {e}\")\n",
    "        return\n",
    "\n",
    "    summarize_dataframe(df)\n",
    "\n",
    "    if 'page_id' in df.columns:\n",
    "        summarize_by_group(df, ['page_id'])\n",
    "\n",
    "    if 'page_id' in df.columns and 'ad_id' in df.columns:\n",
    "        summarize_by_group(df, ['page_id', 'ad_id'])\n",
    "\n",
    "def main():\n",
    "    for name, path in DATASETS.items():\n",
    "        process_file(name, path)\n",
    "\n",
    "if _name_ == \"_main_\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "999afb5b-0d60-462c-b6e5-d00e5ee7ae7f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
