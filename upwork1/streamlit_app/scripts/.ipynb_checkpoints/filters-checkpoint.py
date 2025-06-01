{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d3fd7bb-19f2-41cf-b7a2-1399697465fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# scripts/filters.py\n",
    "import pandas as pd\n",
    "\n",
    "def apply_filters(df, years, regions, dim1):\n",
    "    \"\"\"Apply filters to DataFrame\"\"\"\n",
    "    return df[\n",
    "        (df['Period'].between(years[0], years[1])) &\n",
    "        (df['ParentLocation'].isin(regions)) &\n",
    "        (df['Dim1'].isin(dim1))\n",
    "    ]"
   ]
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
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
