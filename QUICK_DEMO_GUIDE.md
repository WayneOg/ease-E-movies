# 🎬 Quick Demo Guide - Watch Now & Episodes Feature

## 🚀 Both Servers Are Running!

- ✅ **Django Backend**: http://localhost:8000/
- ✅ **React Frontend**: http://localhost:3001/

---

## 🎥 Feature 1: Movie Watch Now

### **How to Test:**

1. **Open the frontend**: http://localhost:3001/
2. **Click on any movie** (e.g., from trending or popular)
3. **Click the "Watch Now" button**

### **What Happens:**

#### **If Movie Has Streaming URLs:**
```
┌─────────────────────────────────────────┐
│  🎬 Movie Title                    ✕    │
│  [Server 1 (Wootly)] [Server 2 (Dood)]  │
├─────────────────────────────────────────┤
│                                         │
│         🎥 VIDEO PLAYER HERE            │
│                                         │
│     (Full-screen embedded player)       │
│                                         │
└─────────────────────────────────────────┘
```

#### **If Movie Has NO Streaming URLs:**
```
┌─────────────────────────────────┐
│  No Stream Available            │
│                                 │
│  Sorry, this content is not     │
│  available for streaming at     │
│  the moment.                    │
│                                 │
│         [Close]                 │
└─────────────────────────────────┘
```

### **To Add Streaming URLs:**

1. Go to: http://localhost:8000/admin/
2. Login with your admin credentials
3. Click **"Movies"** → Find your movie
4. Add URLs to `wootly_url` and/or `dood_url` fields
5. Save and test again!

---

## 📺 Feature 2: Series Episodes Organization

### **How to Test:**

1. **Open the frontend**: http://localhost:3001/
2. **Click "Series"** in the navigation
3. **Click on any TV series**
4. **Scroll down** to see "Seasons & Episodes"

### **What You'll See:**

```
┌─────────────────────────────────────────────────────────┐
│  Seasons & Episodes                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ▼ Season 1                                             │
│     10 Episodes • 2011                                  │
│  ┌───────────────────────────────────────────────────┐ │
│  │ 1  Winter Is Coming                      [Watch]  │ │
│  │    Ned Stark is torn between his family...        │ │
│  │    📅 Apr 17, 2011  ⭐ 8.1                        │ │
│  ├───────────────────────────────────────────────────┤ │
│  │ 2  The Kingsroad                         [Watch]  │ │
│  │    While Bran recovers from his fall...           │ │
│  │    📅 Apr 24, 2011  ⭐ 7.9                        │ │
│  └───────────────────────────────────────────────────┘ │
│                                                         │
│  ▶ Season 2                                             │
│     10 Episodes • 2012                                  │
│                                                         │
│  ▶ Season 3                                             │
│     10 Episodes • 2013                                  │
└─────────────────────────────────────────────────────────┘
```

### **Interactive Features:**

- **Click season header** → Expands/collapses episodes
- **Click "Watch" button** → Plays that specific episode
- **Hover over episodes** → Highlights with smooth animation
- **All episodes ordered** → By season number, then episode number

### **To Add Episodes:**

1. Go to: http://localhost:8000/admin/
2. Click **"Series"** → Select a series
3. Click **"Seasons"** → Add seasons with season numbers
4. For each season, click **"Episodes"** → Add episodes
5. Episodes will automatically appear organized!

---

## 🎯 Quick Test Checklist

### **Movies:**
- [ ] Open any movie detail page
- [ ] Click "Watch Now" button
- [ ] Video player opens full-screen
- [ ] Can switch between servers (if multiple)
- [ ] Can close player with X button
- [ ] Shows "No Stream" message if URLs missing

### **Series:**
- [ ] Open any series detail page
- [ ] See "Seasons & Episodes" section
- [ ] Click season header to expand
- [ ] See all episodes listed in order
- [ ] Each episode shows number, name, description
- [ ] Each episode has "Watch" button
- [ ] Click season header again to collapse

---

## 🔧 Troubleshooting

### **"Watch Now" does nothing:**
- ✅ **Fixed!** The button now opens the video player
- If you see "No Stream Available", add URLs in Django Admin

### **No episodes showing:**
- Episodes must be added to the database via Django Admin
- The API fetches series info from TMDB but episodes from database
- Add seasons and episodes manually for each series

### **Player won't load:**
- Check browser console for errors
- Verify streaming URLs are valid
- Try switching to the other server

### **Seasons not expanding:**
- Check browser console for errors
- Verify series has seasons in database
- Refresh the page

---

## 📊 API Endpoints to Test

### **Movie with Streaming URLs:**
```bash
curl http://localhost:8000/api/movie/550/
```

**Expected Response:**
```json
{
  "id": 550,
  "title": "Fight Club",
  "wootly_url": "https://...",
  "dood_url": "https://...",
  "poster_path": "/...",
  "backdrop_path": "/...",
  "overview": "...",
  "vote_average": 8.4,
  "release_date": "1999-10-15",
  "runtime": 139,
  "genres": [...],
  "tagline": "..."
}
```

### **Series with Episodes:**
```bash
curl http://localhost:8000/api/series/1399/
```

**Expected Response:**
```json
{
  "id": 1399,
  "title": "Game of Thrones",
  "seasons": [
    {
      "id": 1,
      "season_number": 1,
      "name": "Season 1",
      "overview": "...",
      "air_date": "2011-04-17",
      "episode_count": 10,
      "episodes": [
        {
          "id": 1,
          "episode_number": 1,
          "name": "Winter Is Coming",
          "overview": "...",
          "air_date": "2011-04-17",
          "vote_average": 8.1
        }
      ]
    }
  ]
}
```

---

## 🎨 UI Components

### **VideoPlayer Component:**
- Location: `frontend/src/components/VideoPlayer.jsx`
- Features: Full-screen modal, server switching, close button
- Props: `wootlyUrl`, `doodUrl`, `title`, `onClose`

### **Season/Episode UI:**
- Location: `frontend/src/pages/SeriesDetail.jsx`
- Features: Collapsible sections, episode cards, watch buttons
- State: `expandedSeasons` tracks which seasons are open

---

## 🎉 What's Working Now

### ✅ **Movies:**
1. Watch Now button opens video player
2. Multiple server support (Wootly + Dood)
3. Full-screen playback
4. Graceful fallback when no streams available

### ✅ **Series:**
1. Seasons organized by season number
2. Episodes organized by episode number within seasons
3. Collapsible season sections
4. Full episode details (name, description, date, rating)
5. Individual watch buttons per episode
6. Smooth animations and hover effects

---

## 📱 Responsive Design

Both features work perfectly on:
- 💻 **Desktop** - Full-screen experience
- 📱 **Tablet** - Optimized layout
- 📱 **Mobile** - Touch-friendly controls

---

## 🚀 Next Steps

### **To Populate Content:**

1. **Add Movies with Streaming URLs:**
   - Django Admin → Movies → Add/Edit
   - Fill in `wootly_url` and `dood_url`

2. **Add Series Episodes:**
   - Django Admin → Series → Select series
   - Add Seasons → Add Episodes for each season

3. **Test Everything:**
   - Browse movies and click "Watch Now"
   - Browse series and expand seasons
   - Click episode "Watch" buttons

---

## 🎬 Enjoy Your Streaming Platform!

Everything is now working:
- ✅ Movie streaming with Watch Now
- ✅ Series episodes organized by season
- ✅ Beautiful, responsive UI
- ✅ Smooth animations
- ✅ Full-screen video player

**Happy Streaming! 🍿**

---

**Questions?**
- Check `WATCH_NOW_FEATURE_COMPLETE.md` for technical details
- Check Django Admin for content management
- Check browser console for debugging