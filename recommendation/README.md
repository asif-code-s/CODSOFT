# CodSoft Internship – Task 4 ✅

## 🎬 Smart Movie Recommender

This is my fourth project submission for the **CodSoft AI Internship (July Batch 2025)**.  
- This app is a simple yet smart movie recommendation system built using **Python** and **Streamlit**.
- It uses **content-based filtering** with **cosine similarity** to suggest similar movies based on genres.

---

## 💡 Features

- 🔎 **Fuzzy Matching** – Accepts partial or similar movie names (uses `difflib.get_close_matches`)
- 🧠 **Content-Based Recommendations** – Suggests 5 similar movies based on genre similarity
- 🎭 **Genre Explorer** – Lets you explore random movies by selecting a genre
- 🧼 **Reset Button** – Clears all input fields with one click
- 🧑‍💻 **User-Friendly UI** – Clean layout built using **Streamlit**
- 📦 Based on **MovieLens Dataset (100k)**

---

## 📦 Tech Stack

- Python 3
- Pandas
- Scikit-learn
- Streamlit
- Difflib
- Random

---

## 🧪 How It Works

```plaintext
1. Enter a movie name (even partially)
2. OR choose from a dropdown of all movies
3. OR pick a genre to explore related movies
4. System shows 5 similar movie suggestions
5. Reset button clears everything anytime
```

---

## 📁 Dataset Used

- **u.data**: user ratings
- **u.item**: movie titles + 19 genre columns (binary flags)
- Source: [MovieLens 100k dataset]

---

## ✅ Task Requirement Covered

✔️ Built a simple recommendation system  
✔️ Used content-based filtering  
✔️ Suggested movies based on user input  
✔️ Added genre-based exploration  
✔️ Clean, interactive frontend with Streamlit

---

## 📌 Sample Output

```plaintext
🎬 Movie Recommendations for: Toy Story (1995)

1. Babe (1995)
2. Casper (1995)
3. James and the Giant Peach (1996)
4. Aladdin (1992)
5. Lion King, The (1994)

🍿 Movies in Comedy genre:
1. Liar Liar (1997)
2. Jerry Maguire (1996)
3. Nutty Professor, The (1996)
...
```

---

👨‍💻 Submitted by: **Asif Hussain A**  
Internship: **CodSoft – AI (July 2025)**
