<entry path="index.html">
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Holy Quran & Namaz Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #000000;
            --primary-hover: #333333;
            --bg: #ffffff;
            --card-bg: #ffffff;
            --text: #000000;
            --border: #000000;
            --subtext: #444444;
            --alhuda-bg: #ffffff;
            --alhuda-border: #000000;
            --arabic-color: #000000;
            --bookmark-bg: #e6e6e6;
            --bookmark-border: #000000;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #000000;
            color: #ffffff;
            text-align: center;
            padding: 2rem 1rem;
            border-bottom: 2px solid #000000;
        }

        header h1 { margin: 0; font-size: 2.2rem; }
        header p { margin: 0.5rem 0 0 0; opacity: 0.9; }

        .container {
            max-width: 1200px;
            margin: 1.5rem auto;
            padding: 0 1rem;
        }

        /* Navigation Tabs */
        .nav-tabs {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .tab-btn {
            padding: 0.8rem 1.5rem;
            font-size: 1rem;
            font-weight: 600;
            border: 2px solid #000000;
            background: #ffffff;
            color: #000000;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .tab-btn.active, .tab-btn:hover {
            background: #000000;
            color: #ffffff;
        }

        .bookmark-banner {
            background: var(--bookmark-bg);
            border: 2px solid var(--bookmark-border);
            padding: 0.8rem 1.2rem;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            font-weight: 600;
            color: #000000;
        }

        .bookmark-banner button {
            background: #000000;
            color: #ffffff;
            border: none;
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
            cursor: pointer;
        }

        .pages-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
            gap: 1rem;
        }

        .page-card {
            background: var(--card-bg);
            padding: 1.2rem;
            border-radius: 10px;
            border: 2px solid var(--border);
            text-align: center;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
            font-weight: 600;
            position: relative;
            color: #000000;
        }

        .page-card:hover {
            transform: translateY(-3px);
            background: #f0f0f0;
        }

        .page-card.marked::after {
            content: "🔖 Marked";
            position: absolute;
            top: 4px;
            right: 4px;
            font-size: 0.65rem;
            background: #000000;
            color: #ffffff;
            padding: 2px 4px;
            border-radius: 4px;
        }

        #reader-view, #namaz-view {
            display: none;
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 16px;
            border: 2px solid var(--border);
        }

        .back-btn {
            background: #000000;
            color: #ffffff;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
        }

        .mark-read-btn {
            background: #ffffff;
            color: #000000;
            border: 2px solid #000000;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }

        .mark-read-btn.active {
            background: #000000;
            color: #ffffff;
        }

        .namaz-card {
            background: var(--card-bg);
            border: 2px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .namaz-card h3 {
            margin-top: 0;
            color: #000000;
            border-bottom: 2px solid var(--border);
            padding-bottom: 0.5rem;
        }

        .transliteration {
            font-style: italic;
            color: var(--subtext);
            margin: 0.5rem 0;
        }

        .page-navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            gap: 1rem;
            flex-wrap: wrap;
        }

        /* Pure White Background Frame */
        .quran-frame {
            background-color: var(--alhuda-bg);
            padding: 2rem;
            border-radius: 12px;
            border: 2px solid var(--border);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            min-height: 500px;
        }

        /* Written Arabic Typography */
        .written-arabic-container {
            direction: rtl;
            text-align: justify;
            text-align-last: center;
            font-family: 'Amiri', serif;
            font-size: 2rem;
            line-height: 3.8rem;
            color: var(--arabic-color);
            padding: 1rem 0;
        }

        .surah-header-block {
            text-align: center;
            background: #ffffff;
            border: 2px solid var(--alhuda-border);
            border-radius: 8px;
            padding: 0.8rem;
            margin: 1.5rem 0;
            font-size: 1.8rem;
            font-weight: bold;
            color: #000000;
        }

        .bismillah-block {
            text-align: center;
            font-size: 2.2rem;
            margin: 1rem 0 1.5rem 0;
            color: #000000;
        }

        .ayah-container {
            display: inline;
            cursor: pointer;
            padding: 2px 4px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }

        .ayah-container:hover {
            background-color: #eeeeee;
        }

        .ayah-container.last-read-ayah {
            background-color: var(--bookmark-bg);
            border-bottom: 2px dashed var(--bookmark-border);
        }

        .ayah-container.playing-ayah {
            background-color: #c8e6c9 !important;
            border-radius: 6px;
        }

        .ayah-number {
            display: inline-block;
            font-size: 1.2rem;
            color: #000000;
            margin: 0 0.4rem;
            border: 1px solid #000000;
            border-radius: 50%;
            width: 2.2rem;
            height: 2.2rem;
            line-height: 2.2rem;
            text-align: center;
        }

        .loading-text {
            text-align: center;
            font-size: 1.2rem;
            color: var(--subtext);
            padding: 3rem;
        }

        .audio-player-controls {
            margin-top: 1.5rem;
            background: var(--bg);
            padding: 1.2rem;
            border-radius: 12px;
            border: 2px solid var(--border);
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
        }

        .audio-btn-group {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .play-main-btn {
            background: #000000;
            color: #ffffff;
            border: none;
            padding: 0.7rem 1.5rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .play-main-btn:hover {
            background: #333333;
        }

        .audio-seeker {
            width: 100%;
            height: 8px;
            cursor: pointer;
            accent-color: #000000;
            border-radius: 4px;
        }

        .status-badge {
            font-size: 0.85rem;
            color: var(--subtext);
            font-weight: 600;
        }
    </style>
</head>
<body>

    <header>
        <h1 id="main-title">The Holy Quran & Namaz Portal</h1>
        <p id="sub-title">Al Huda Quran & Recitation by Qari Mishary Rashid Alafasy</p>
    </header>

    <div class="container">
        <!-- Navigation -->
        <div class="nav-tabs">
            <button class="tab-btn active" id="tab-quran" onclick="switchTab('quran')">Holy Quran</button>
            <button class="tab-btn" id="tab-namaz" onclick="switchTab('namaz')">All Namaz Guide</button>
        </div>

        <!-- Saved Reading Bookmark Banner -->
        <div id="bookmark-banner" class="bookmark-banner" style="display: none;">
            <div>
                🔖 <strong>Last Read Position Saved:</strong> <span id="bookmark-info">Page 1</span>
            </div>
            <button onclick="goToLastBookmark()">Resume Reading →</button>
        </div>

        <!-- Quran Pages Grid View -->
        <div id="main-view">
            <h2 style="color: #000000; text-align: center; margin-bottom: 1.5rem;">Select Page (1 to 604)</h2>
            <div class="pages-grid" id="pages-list"></div>
        </div>

        <!-- Quran Reader View -->
        <div id="reader-view">
            <div class="page-navigation">
                <button class="back-btn" onclick="showMainView()">← Back to Pages</button>
                <h3 id="current-page-title" style="margin: 0; color: #000000;">Page 1</h3>
                <div>
                    <button class="mark-read-btn" id="mark-page-btn" onclick="togglePageMark()">
                        📌 Mark Page as Read
                    </button>
                    <button class="back-btn" onclick="changePage(-1)">← Prev</button>
                    <button class="back-btn" onclick="changePage(1)">Next →</button>
                </div>
            </div>

            <div class="quran-frame">
                <!-- Pure Written Arabic Text Display -->
                <div id="written-arabic-view" class="written-arabic-container"></div>
            </div>

            <!-- Audio Player Controls & Interactive Seeker Bar -->
            <div class="audio-player-controls">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0; color: #000000;">Recitation: Qari Mishary Rashid Alafasy</h4>
                    <span id="audio-status" class="status-badge">Ready to Play</span>
                </div>
                <div class="audio-btn-group">
                    <button id="toggle-audio-btn" class="play-main-btn" onclick="toggleAudioPlayback()">
                        ▶ Play Audio
                    </button>
                    <p style="margin: 0; font-size: 0.85rem; color: #555;">(Click any verse to listen directly or adjust audio position using the slider)</p>
                </div>
                <input type="range" id="audio-seekbar" class="audio-seeker" value="0" min="0" max="100" oninput="seekAudio(this.value)">
                <audio id="page-audio" crossorigin="anonymous"></audio>
            </div>
        </div>

        <!-- All Namaz & Prayer Guide View -->
        <div id="namaz-view">
            <h2 style="color: #000000; text-align: center; margin-bottom: 2rem;">Complete Prayer Guide (Namaz & Duas)</h2>
            <div id="namaz-content"></div>
        </div>
    </div>

    <script>
        let currentPage = 1;
        let lastReadBookmark = JSON.parse(localStorage.getItem('quran_last_read')) || null;
        let currentAyahsList = [];
        let currentAyahIndex = 0;
        let isPlaying = false;

        const pageAudio = document.getElementById('page-audio');
        const toggleAudioBtn = document.getElementById('toggle-audio-btn');
        const audioSeekbar = document.getElementById('audio-seekbar');
        const audioStatus = document.getElementById('audio-status');

        pageAudio.addEventListener('ended', () => {
            if (currentAyahIndex < currentAyahsList.length - 1) {
                playVerseAtIndex(currentAyahIndex + 1);
            } else {
                stopAudio();
                audioStatus.innerText = "Completed Page";
            }
        });

        pageAudio.addEventListener('error', (e) => {
            console.error("Audio playback error:", e);
            audioStatus.innerText = "Audio load error - click verse to try again";
        });

        function updateSeekbar() {
            if (currentAyahsList.length > 0) {
                const progress = ((currentAyahIndex + 1) / currentAyahsList.length) * 100;
                audioSeekbar.value = progress;
            }
        }

        function toggleAudioPlayback() {
            if (isPlaying) {
                pageAudio.pause();
                isPlaying = false;
                toggleAudioBtn.innerHTML = '▶ Play Audio';
                audioStatus.innerText = 'Paused';
            } else {
                if (currentAyahsList.length > 0) {
                    playVerseAtIndex(currentAyahIndex);
                }
            }
        }

        function playVerseAtIndex(index) {
            if (index < 0 || index >= currentAyahsList.length) return;
            currentAyahIndex = index;
            const ayah = currentAyahsList[index];

            highlightCurrentAyah(ayah);
            updateSeekbar();

            // Direct audio URL from Alafasy CDN
            pageAudio.src = ayah.audio || `https://cdn.islamic.network/quran/audio/128/ar.alafasy/${ayah.number}.mp3`;
            
            pageAudio.play().then(() => {
                isPlaying = true;
                toggleAudioBtn.innerHTML = '⏸ Pause Audio';
                audioStatus.innerText = `Playing Verse ${ayah.numberInSurah} of Surah ${ayah.surah.englishName}`;
            }).catch(err => {
                console.log("Play failed:", err);
                audioStatus.innerText = "Press Play to start audio";
            });
        }

        function stopAudio() {
            pageAudio.pause();
            isPlaying = false;
            toggleAudioBtn.innerHTML = '▶ Play Audio';
            removeHighlight();
        }

        function seekAudio(value) {
            if (currentAyahsList.length > 0) {
                const targetIndex = Math.min(
                    Math.floor((value / 100) * currentAyahsList.length),
                    currentAyahsList.length - 1
                );
                playVerseAtIndex(targetIndex);
            }
        }

        function highlightCurrentAyah(ayah) {
            removeHighlight();
            const ayahKey = `${ayah.surah.number}_${ayah.numberInSurah}`;
            const el = document.getElementById(`ayah-${ayahKey}`);
            if (el) {
                el.classList.add('playing-ayah');
                el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        }

        function removeHighlight() {
            document.querySelectorAll('.ayah-container').forEach(el => el.classList.remove('playing-ayah'));
        }

        function switchTab(tab) {
            stopAudio();
            document.getElementById('reader-view').style.display = 'none';
            document.getElementById('tab-quran').classList.remove('active');
            document.getElementById('tab-namaz').classList.remove('active');

            if (tab === 'quran') {
                document.getElementById('tab-quran').classList.add('active');
                document.getElementById('main-view').style.display = 'block';
                document.getElementById('namaz-view').style.display = 'none';
                checkBookmarkBanner();
            } else {
                document.getElementById('tab-namaz').classList.add('active');
                document.getElementById('main-view').style.display = 'none';
                document.getElementById('namaz-view').style.display = 'block';
                renderNamazGuide();
            }
        }

        function checkBookmarkBanner() {
            const banner = document.getElementById('bookmark-banner');
            if (lastReadBookmark) {
                banner.style.display = 'flex';
                let text = `Page ${lastReadBookmark.page}`;
                if (lastReadBookmark.ayahNum) {
                    text += ` (Verse ${lastReadBookmark.ayahNum})`;
                }
                document.getElementById('bookmark-info').innerText = text;
            } else {
                banner.style.display = 'none';
            }
        }

        function goToLastBookmark() {
            if (lastReadBookmark) {
                openPage(lastReadBookmark.page, lastReadBookmark.ayahKey);
            }
        }

        function renderPagesGrid() {
            const container = document.getElementById('pages-list');
            container.innerHTML = '';

            for (let i = 1; i <= 604; i++) {
                const card = document.createElement('div');
                card.className = 'page-card';
                if (lastReadBookmark && lastReadBookmark.page === i) {
                    card.classList.add('marked');
                }
                card.innerText = `Page ${i}`;
                card.onclick = () => openPage(i);
                container.appendChild(card);
            }
        }

        function togglePageMark() {
            if (lastReadBookmark && lastReadBookmark.page === currentPage && !lastReadBookmark.ayahKey) {
                lastReadBookmark = null;
                localStorage.removeItem('quran_last_read');
            } else {
                lastReadBookmark = { page: currentPage, ayahKey: null, ayahNum: null };
                localStorage.setItem('quran_last_read', JSON.stringify(lastReadBookmark));
            }
            updateMarkButtonState();
            checkBookmarkBanner();
            renderPagesGrid();
        }

        function updateMarkButtonState() {
            const btn = document.getElementById('mark-page-btn');
            if (lastReadBookmark && lastReadBookmark.page === currentPage) {
                btn.classList.add('active');
                btn.innerHTML = '✔ Marked as Last Read';
            } else {
                btn.classList.remove('active');
                btn.innerHTML = '📌 Mark Page as Read';
            }
        }

        function markAyahAsRead(page, surahNum, ayahNum, ayahKey, index) {
            lastReadBookmark = { page, surahNum, ayahNum, ayahKey };
            localStorage.setItem('quran_last_read', JSON.stringify(lastReadBookmark));
            
            document.querySelectorAll('.ayah-container').forEach(el => el.classList.remove('last-read-ayah'));
            const target = document.getElementById(`ayah-${ayahKey}`);
            if (target) target.classList.add('last-read-ayah');

            updateMarkButtonState();
            checkBookmarkBanner();
            renderPagesGrid();
            
            // Play audio from clicked verse
            playVerseAtIndex(index);
        }

        function stripBismillah(text) {
            const bismillahVariations = [
                'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ',
                'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ',
                'بِسمِ اللَّهِ الرَّحمٰنِ الرَّحيمِ'
            ];

            let cleanedText = text;
            bismillahVariations.forEach(bismillah => {
                if (cleanedText.startsWith(bismillah)) {
                    cleanedText = cleanedText.replace(bismillah, '').trim();
                }
            });

            return cleanedText;
        }

        async function fetchWrittenArabicPage(pageNum, targetAyahKey = null) {
            const container = document.getElementById('written-arabic-view');
            container.innerHTML = '<div class="loading-text">Loading Quran Page Text & Audio...</div>';

            try {
                // Fetch page text alongside Mishary Rashid Alafasy audio endpoint
                const response = await fetch(`https://api.alquran.cloud/v1/page/${pageNum}/ar.alafasy`);
                const data = await response.json();

                if (data.code === 200 && data.data.ayahs) {
                    container.innerHTML = '';
                    currentAyahsList = data.data.ayahs;
                    currentAyahIndex = 0;
                    let currentSurahNumber = null;

                    data.data.ayahs.forEach((ayah, index) => {
                        if (ayah.surah.number !== currentSurahNumber) {
                            currentSurahNumber = ayah.surah.number;
                            const surahHeader = document.createElement('div');
                            surahHeader.className = 'surah-header-block';
                            surahHeader.innerText = `سُورَةُ ${ayah.surah.name}`;
                            container.appendChild(surahHeader);

                            if (currentSurahNumber !== 9 && currentSurahNumber !== 1) {
                                const bismillah = document.createElement('div');
                                bismillah.className = 'bismillah-block';
                                bismillah.innerText = 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ';
                                container.appendChild(bismillah);
                            }
                        }

                        let text = ayah.text;

                        if (ayah.numberInSurah === 1 && currentSurahNumber !== 1) {
                            text = stripBismillah(text);
                        }

                        const ayahKey = `${ayah.surah.number}_${ayah.numberInSurah}`;
                        const verseSpan = document.createElement('span');
                        verseSpan.className = 'ayah-container';
                        verseSpan.id = `ayah-${ayahKey}`;
                        
                        if (lastReadBookmark && lastReadBookmark.ayahKey === ayahKey) {
                            verseSpan.classList.add('last-read-ayah');
                        }

                        verseSpan.title = "Click verse to listen and mark as read";
                        verseSpan.onclick = () => markAyahAsRead(pageNum, ayah.surah.number, ayah.numberInSurah, ayahKey, index);
                        verseSpan.innerHTML = `${text} <span class="ayah-number">${ayah.numberInSurah}</span> `;
                        container.appendChild(verseSpan);
                    });

                    audioStatus.innerText = "Ready to Play";

                    if (targetAyahKey) {
                        setTimeout(() => {
                            const target = document.getElementById(`ayah-${targetAyahKey}`);
                            if (target) target.scrollIntoView({ behavior: 'smooth', block: 'center' });
                        }, 200);
                    }
                } else {
                    container.innerHTML = '<div class="loading-text">Failed to load text. Please check connection.</div>';
                }
            } catch (err) {
                container.innerHTML = '<div class="loading-text">Unable to load Arabic text and audio. Check network connection.</div>';
            }
        }

        function openPage(pageNum, targetAyahKey = null) {
            if (pageNum < 1) pageNum = 1;
            if (pageNum > 604) pageNum = 604;
            currentPage = pageNum;

            stopAudio();
            audioSeekbar.value = 0;

            document.getElementById('main-view').style.display = 'none';
            document.getElementById('reader-view').style.display = 'block';
            document.getElementById('current-page-title').innerText = `Page ${currentPage} of 604`;

            updateMarkButtonState();
            fetchWrittenArabicPage(currentPage, targetAyahKey);

            if (!targetAyahKey) {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        function changePage(delta) {
            openPage(currentPage + delta);
        }

        function showMainView() {
            stopAudio();
            document.getElementById('reader-view').style.display = 'none';
            document.getElementById('main-view').style.display = 'block';
            checkBookmarkBanner();
            renderPagesGrid();
        }

        const namazData = [
            {
                title: "1. Niyyah (Intention)",
                arabic: "نَوَيْتُ أَنْ أُصَلِّيَ لِلَّهِ تَعَالَى رَكَعَاتِ صَلَاةِ...",
                transliteration: "Nawaytu an usalliya lillahi ta'ala rak'ati salat...",
                translation: "I intend to pray for Allah the Almighty..."
            },
            {
                title: "2. Takbeer-e-Tahreema",
                arabic: "اللهُ أَكْبَرُ",
                transliteration: "Allahu Akbar",
                translation: "Allah is the Greatest."
            },
            {
                title: "3. Thana (Opening Dua)",
                arabic: "سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ وَتَبَارَكَ اسْمُكَ وَتَعَالَى جَدُّكَ وَلَا إِلَهَ غَيْرُكَ",
                transliteration: "Subhanakal-lahumma wa bihamdika wa tabarakasmuka wa ta'ala jadduka wa la ilaha ghayruk.",
                translation: "Glory be to You, O Allah, and all praise is Yours. Blessed is Your name, exalted is Your majesty, and there is no deity worthy of worship besides You."
            },
            {
                title: "4. Surah Al-Fatiha (Recited in Every Rakat)",
                arabic: "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ ﴿١﴾ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ ﴿٢﴾ الرَّحْمَنِ الرَّحِيمِ ﴿٣﴾ مَالِكِ يَوْمِ الدِّينِ ﴿٤﴾ إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ ﴿٥﴾ اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ ﴿٦﴾ صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ ﴿٧﴾",
                transliteration: "Bismillaahir-Rahmaanir-Raheem. Alhamdu lillaahi Rabbil-'aalameen...",
                translation: "In the name of Allah, the Most Gracious, the Most Merciful. All praise is due to Allah, Lord of the worlds..."
            },
            {
                title: "5. Ruku (Bowing)",
                arabic: "سُبْحَانَ رَبِّيَ الْعَظِيمِ",
                transliteration: "Subhana Rabbiyal-Azeem (3 times)",
                translation: "Glory be to my Lord, the Most Great."
            },
            {
                title: "6. Qiyam (Rising from Ruku)",
                arabic: "سَمِعَ اللَّهُ لِمَنْ حَمِدَهُ - رَبَّنَا وَلَكَ الْحَمْدُ",
                transliteration: "Sami'allahu liman hamidah - Rabbana wa lakal-hamd",
                translation: "Allah hears whoever praises Him - Our Lord, all praise belongs to You."
            },
            {
                title: "7. Sujood (Prostration)",
                arabic: "سُبْحَانَ رَبِّيَ الْأَعْلَى",
                transliteration: "Subhana Rabbiyal-A'la (3 times)",
                translation: "Glory be to My Lord, the Most High."
            },
            {
                title: "8. Tashahhud (Sitting Position)",
                arabic: "التَّحِيَّاتُ لِلَّهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ ، السَّلاَمُ عَلَيْكَ أَيُّهَا النَّبِيُّ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ ، السَّلاَمُ عَلَيْنَا وَعَلَى عِبَادِ اللَّهِ الصَّالِحِينَ ، أَشْهَدُ أَنْ لاَ إِلَهَ إِلاَّ اللَّهُ وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ",
                transliteration: "At-tahiyyatu lillahi was-salawatu wat-tayyibat...",
                translation: "All compliments, prayers, and pure actions are due to Allah. Peace be upon you, O Prophet, and the mercy of Allah and His blessings..."
            },
            {
                title: "9. Durood Ibrahim",
                arabic: "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ إِنَّكَ حَمِيدٌ مَجِيدٌ",
                transliteration: "Allahumma salli 'ala Muhammadin wa 'ala ali Muhammadin...",
                translation: "O Allah, send blessings upon Muhammad and upon the family of Muhammad, as You sent blessings upon Ibrahim..."
            },
            {
                title: "10. Tasleem (Ending Prayer)",
                arabic: "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ",
                transliteration: "Assalamu alaykum wa rahmatullah (Right & Left)",
                translation: "Peace and mercy of Allah be upon you."
            }
        ];

        function renderNamazGuide() {
            const container = document.getElementById('namaz-content');
            container.innerHTML = '';

            namazData.forEach(item => {
                const card = document.createElement('div');
                card.className = 'namaz-card';
                card.innerHTML = `
                    <h3>${item.title}</h3>
                    <div style="font-family: 'Amiri', serif; direction: rtl; text-align: right; font-size: 2rem; line-height: 3.5rem; margin-bottom: 0.5rem;" dir="rtl">${item.arabic}</div>
                    <div class="transliteration"><strong>Transliteration:</strong> ${item.transliteration}</div>
                    <div class="translation-text"><strong>Translation:</strong> ${item.translation}</div>
                `;
                container.appendChild(card);
            });
        }

        renderPagesGrid();
        checkBookmarkBanner();
    </script>
</body>
</html>
</entry>
