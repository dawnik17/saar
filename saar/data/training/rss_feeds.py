rss_feeds = [
    "http://feeds.bbci.co.uk/news/rss.xml",  # BBC News
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",  # The New York Times - World News
    "http://feeds.reuters.com/reuters/topNews",  # Reuters - Top News
    "https://news.ycombinator.com/rss",  # Hacker News
    "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss",  # NASA News
    "https://www.espn.com/espn/rss/news",  # ESPN - Top Headlines
    "http://feeds.feedburner.com/TechCrunch",  # TechCrunch
    "https://feeds.feedburner.com/time/topstories",  # TIME Magazine - Top Stories
    "https://www.economist.com/the-world-this-week/rss.xml",  # The Economist - The World This Week
    "https://rss.cbc.ca/lineup/topstories.xml",  # CBC News - Top Stories
    "https://www.theguardian.com/world/rss",  # The Guardian - World News
    "https://www.aljazeera.com/xml/rss/all.xml",  # Al Jazeera - All News
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",  # CNBC - Top News
    "https://feeds.npr.org/1001/rss.xml",  # NPR - Top Stories
    "https://www.wsj.com/xml/rss/3_7085.xml",  # The Wall Street Journal - World News
    "https://feeds.a.dj.com/rss/RSSOpinion.xml",  # The Wall Street Journal - Opinion
    "http://www.sciencemag.org/rss/news_current.xml",  # Science Magazine - Current News
    "https://www.wired.com/feed/rss",  # WIRED - Top Stories
    "https://www.ft.com/rss/world",  # Financial Times - World News
    "https://www.business-standard.com/rss/latest.rss",  # Business Standard - Latest News
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",  # The Times of India - Top Stories
    "https://feeds.feedburner.com/daily-express-news-showbiz",  # Daily Express - News and Showbiz
    "https://www.independent.co.uk/news/rss",  # The Independent - News
    "https://rss.dw.com/rdf/rss-en-all",  # Deutsche Welle - Top Stories
    "https://www.voanews.com/api/zq$omekvi",  # Voice of America - Top Stories
    "https://www.theonion.com/rss",  # The Onion - Top Stories (Satire)
    "https://www.nationalgeographic.com/latest-stories/_jcr_content/header/main-feed.rss",  # National Geographic - Latest Stories
    "https://rss.sciam.com/sciam/mind-and-brain",  # Scientific American - Mind & Brain
    "https://www.buzzfeed.com/world.xml",  # BuzzFeed News - World
    "https://www.vox.com/rss/world/index.xml",  # Vox - World
    "https://www.recode.net/rss/index.xml",  # Recode - All Stories
    "https://www.bloomberg.com/opinion/feeds/contributors/qEVx3vBKUc4/rss.xml",  # Bloomberg Opinion
    "https://www.vice.com/en_us/rss",  # VICE - News
    "https://rssfeeds.usatoday.com/usatoday-NewsTopStories",  # USA TODAY - Top Stories
    "https://abcnews.go.com/abcnews/topstories",  # ABC News - Top Stories
    "https://www.latimes.com/rss2.0.xml",  # Los Angeles Times - Top News
    "https://feeds.skynews.com/feeds/rss/home.xml",  # Sky News - Home
    "https://www.theverge.com/rss/index.xml",  # The Verge - All Stories
    "https://apnews.com/rss",  # Associated Press - Top News
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",  # The New York Times - Home Page
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",  # The New York Times - Technology
    "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml",  # The New York Times - Science
    "https://rss.nytimes.com/services/xml/rss/nyt/Health.xml",  # The New York Times - Health
    "https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml",  # The New York Times - Arts
    "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",  # The New York Times - Business
    "https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",  # The New York Times - Sports
    "https://rss.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml",  # The New York Times - Fashion & Style
    "https://rss.nytimes.com/services/xml/rss/nyt/Books.xml",  # The New York Times - Books
    "https://rss.nytimes.com/services/xml/rss/nyt/Theater.xml",  # The New York Times - Theater
    "https://rss.nytimes.com/services/xml/rss/nyt/Movies.xml",  # The New York Times - Movies
    "https://rss.nytimes.com/services/xml/rss/nyt/Travel.xml",  # The New York Times - Travel
    "https://rss.nytimes.com/services/xml/rss/nyt/RealEstate.xml",  # The New York Times - Real Estate
    "https://rss.nytimes.com/services/xml/rss/nyt/Automobiles.xml",  # The New York Times - Automobiles
    "https://rss.nytimes.com/services/xml/rss/nyt/Food.xml",  # The New York Times - Food
    "https://rss.nytimes.com/services/xml/rss/nyt/Wine.xml",  # The New York Times - Wine
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceandHealth.xml",  # The New York Times - Science & Health
    "https://rss.nytimes.com/services/xml/rss/nyt/HomeandGarden.xml",  # The New York Times - Home & Garden
    "https://rss.nytimes.com/services/xml/rss/nyt/TMagazine.xml",  # The New York Times - T Magazine
    "https://rss.nytimes.com/services/xml/rss/nyt/Magazine.xml",  # The New York Times - Magazine
    "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml",  # The New York Times - Climate
    "https://rss.nytimes.com/services/xml/rss/nyt/Podcasts.xml",  # The New York Times - Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/ReaderCenter.xml",  # The New York Times - Reader Center
    "https://rss.nytimes.com/services/xml/rss/nyt/Upshot.xml",  # The New York Times - Upshot
    "https://rss.nytimes.com/services/xml/rss/nyt/TheLearningNetwork.xml",  # The New York Times - The Learning Network
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReview.xml",  # The New York Times - Sunday Review
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml",  # The New York Times - International Home
    "https://rss.nytimes.com/services/xml/rss/nyt/Australia.xml",  # The New York Times - Australia
    "https://rss.nytimes.com/services/xml/rss/nyt/Canada.xml",  # The New York Times - Canada
    "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml",  # The New York Times - Europe
    "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",  # The New York Times - Middle East
    "https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml",  # The New York Times - Africa
    "https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml",  # The New York Times - Asia Pacific
    "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml",  # The New York Times - Americas
    "https://rss.nytimes.com/services/xml/rss/nyt/Dealbook.xml",  # The New York Times - Dealbook
    "https://rss.nytimes.com/services/xml/rss/nyt/FirstDraft.xml",  # The New York Times - First Draft
    "https://rss.nytimes.com/services/xml/rss/nyt/YourMoney.xml",  # The New York Times - Your Money
    "https://rss.nytimes.com/services/xml/rss/nyt/Well.xml",  # The New York Times - Well
    "https://rss.nytimes.com/services/xml/rss/nyt/Corrections.xml",  # The New York Times - Corrections
    "https://rss.nytimes.com/services/xml/rss/nyt/TechnologyEmail.xml",  # The New York Times - Technology Email
    "https://rss.nytimes.com/services/xml/rss/nyt/SmarterLiving.xml",  # The New York Times - Smarter Living
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail.xml",  # The New York Times - Science Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekend.xml",  # The New York Times - The Weekend
    "https://rss.nytimes.com/services/xml/rss/nyt/CaliforniaToday.xml",  # The New York Times - California Today
    "https://rss.nytimes.com/services/xml/rss/nyt/NewYorkToday.xml",  # The New York Times - New York Today
    "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml",  # The New York Times - Politics
    "https://rss.nytimes.com/services/xml/rss/nyt/Washington.xml",  # The New York Times - Washington
    "https://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml",  # The New York Times - NY Region
    "https://rss.nytimes.com/services/xml/rss/nyt/Oregon.xml",  # The New York Times - Oregon
    "https://rss.nytimes.com/services/xml/rss/nyt/Healthcare.xml",  # The New York Times - Healthcare
    "https://rss.nytimes.com/services/xml/rss/nyt/ClimateForward.xml",  # The New York Times - Climate Forward
    "https://rss.nytimes.com/services/xml/rss/nyt/RaceRelated.xml",  # The New York Times - Race/Related
    "https://rss.nytimes.com/services/xml/rss/nyt/TheDaily.xml",  # The New York Times - The Daily
    "https://rss.nytimes.com/services/xml/rss/nyt/SportsMonday.xml",  # The New York Times - Sports Monday
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayBusiness.xml",  # The New York Times - Sunday Business
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayStyles.xml",  # The New York Times - Sunday Styles
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceTake.xml",  # The New York Times - ScienceTake
    "https://rss.nytimes.com/services/xml/rss/nyt/TheLivesTheyLived.xml",  # The New York Times - The Lives They Lived
    "https://rss.nytimes.com/services/xml/rss/nyt/WellFamily.xml",  # The New York Times - Well Family
    "https://rss.nytimes.com/services/xml/rss/nyt/MagazineEmail.xml",  # The New York Times - Magazine Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLove.xml",  # The New York Times - Modern Love
    "https://rss.nytimes.com/services/xml/rss/nyt/BooksEmail.xml",  # The New York Times - Books Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BookReview.xml",  # The New York Times - Book Review
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/FashionEmail.xml",  # The New York Times - Fashion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodEmail.xml",  # The New York Times - Food Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TravelEmail.xml",  # The New York Times - Travel Email
    "https://rss.nytimes.com/services/xml/rss/nyt/HomeEmail.xml",  # The New York Times - Home Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Crossword.xml",  # The New York Times - Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/RealEstateEmail.xml",  # The New York Times - Real Estate Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Games.xml",  # The New York Times - Games
    "https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",  # The New York Times - Personal Tech
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsletterToday.xml",  # The New York Times - Newsletter Today
    "https://rss.nytimes.com/services/xml/rss/nyt/NewslettersandAlerts.xml",  # The New York Times - Newsletters and Alerts
    "https://rss.nytimes.com/services/xml/rss/nyt/SpecialSections.xml",  # The New York Times - Special Sections
    "https://rss.nytimes.com/services/xml/rss/nyt/MobileApplications.xml",  # The New York Times - Mobile Applications
    "https://rss.nytimes.com/services/xml/rss/nyt/Video.xml",  # The New York Times - Video
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefing.xml",  # The New York Times - Daily Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeek.xml",  # The New York Times - The Week
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsEvent.xml",  # The New York Times - News Event
    "https://rss.nytimes.com/services/xml/rss/nyt/Audio.xml",  # The New York Times - Audio
    "https://rss.nytimes.com/services/xml/rss/nyt/MorningBriefing.xml",  # The New York Times - Morning Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/EveningBriefing.xml",  # The New York Times - Evening Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/MiniCrossword.xml",  # The New York Times - Mini Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/Opinion.xml",  # The New York Times - Opinion
    "https://rss.nytimes.com/services/xml/rss/nyt/ReaderCenterPodcasts.xml",  # The New York Times - Reader Center Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/FrontPage.xml",  # The New York Times - Front Page
    "https://rss.nytimes.com/services/xml/rss/nyt/BehindTheCover.xml",  # The New York Times - Behind The Cover
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekly.xml",  # The New York Times - The Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewPodcasts.xml",  # The New York Times - Sunday Review Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/WeekendRead.xml",  # The New York Times - Weekend Read
    "https://rss.nytimes.com/services/xml/rss/nyt/Privacy.xml",  # The New York Times - Privacy
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordEmail.xml",  # The New York Times - Crossword Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BusinessEmail.xml",  # The New York Times - Business Email
    "https://rss.nytimes.com/services/xml/rss/nyt/OpinionEmail.xml",  # The New York Times - Opinion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekEmail.xml",  # The New York Times - The Week Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail2020.xml",  # The New York Times - Science Email 2020
    "https://rss.nytimes.com/services/xml/rss/nyt/ForeignAffairs.xml",  # The New York Times - Foreign Affairs
    "https://rss.nytimes.com/services/xml/rss/nyt/Elections.xml",  # The New York Times - Elections
    "https://rss.nytimes.com/services/xml/rss/nyt/Postcards.xml",  # The New York Times - Postcards
    "https://rss.nytimes.com/services/xml/rss/nyt/Magazine.xml",  # The New York Times - Magazine
    "https://rss.nytimes.com/services/xml/rss/nyt/Parenting.xml",  # The New York Times - Parenting
    "https://rss.nytimes.com/services/xml/rss/nyt/HealthcareEmail.xml",  # The New York Times - Healthcare Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekender.xml",  # The New York Times - The Weekender
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/SmarterLivingEmail.xml",  # The New York Times - Smarter Living Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BestofLateNight.xml",  # The New York Times - Best of Late Night
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLovePodcast.xml",  # The New York Times - Modern Love Podcast
    "https://rss.nytimes.com/services/xml/rss/nyt/Heard.xml",  # The New York Times - Heard
    "https://rss.nytimes.com/services/xml/rss/nyt/Morning.xml",  # The New York Times - Morning
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayRead.xml",  # The New York Times - Sunday Read
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewEmail.xml",  # The New York Times - Sunday Review Email
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordExpress.xml",  # The New York Times - Crossword Express
    "https://rss.nytimes.com/services/xml/rss/nyt/Spirituality.xml",  # The New York Times - Spirituality
    "https://rss.nytimes.com/services/xml/rss/nyt/Champions.xml",  # The New York Times - Champions
    "https://rss.nytimes.com/services/xml/rss/nyt/Newsletter.xml",  # The New York Times - Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/InTheLoop.xml",  # The New York Times - In The Loop
    "https://rss.nytimes.com/services/xml/rss/nyt/Laurels.xml",  # The New York Times - Laurels
    "https://rss.nytimes.com/services/xml/rss/nyt/Working.xml",  # The New York Times - Working
    "https://rss.nytimes.com/services/xml/rss/nyt/Watching.xml",  # The New York Times - Watching
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/Wellness.xml",  # The New York Times - Wellness
    "https://rss.nytimes.com/services/xml/rss/nyt/ClimateHub.xml",  # The New York Times - Climate Hub
    "https://rss.nytimes.com/services/xml/rss/nyt/Podcasts.xml",  # The New York Times - Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/ReadersCenters.xml",  # The New York Times - Readers Centers
    "https://rss.nytimes.com/services/xml/rss/nyt/AtWar.xml",  # The New York Times - At War
    "https://rss.nytimes.com/services/xml/rss/nyt/RebeccaZamolo.xml",  # The New York Times - Rebecca Zamolo
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyNewsletter.xml",  # The New York Times - Daily Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/College.xml",  # The New York Times - College
    "https://rss.nytimes.com/services/xml/rss/nyt/Whistleblower.xml",  # The New York Times - Whistleblower
    "https://rss.nytimes.com/services/xml/rss/nyt/TheNewYorkTimes.xml",  # The New York Times - The New York Times
    "https://rss.nytimes.com/services/xml/rss/nyt/OnlineMarketplace.xml",  # The New York Times - Online Marketplace
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefings.xml",  # The New York Times - Daily Briefings
    "https://rss.nytimes.com/services/xml/rss/nyt/MyNewYork.xml",  # The New York Times - My New York
    "https://rss.nytimes.com/services/xml/rss/nyt/GlobalSports.xml",  # The New York Times - Global Sports
    "https://rss.nytimes.com/services/xml/rss/nyt/AboutOurAds.xml",  # The New York Times - About Our Ads
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordDaily.xml",  # The New York Times - Crossword Daily
    "https://rss.nytimes.com/services/xml/rss/nyt/Stop.xml",  # The New York Times - Stop
    "https://rss.nytimes.com/services/xml/rss/nyt/CaliforniaSunday.xml",  # The New York Times - California Sunday
    "https://rss.nytimes.com/services/xml/rss/nyt/NextDoor.xml",  # The New York Times - Next Door
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail2020.xml",  # The New York Times - Science Email 2020
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/BigCity.xml",  # The New York Times - Big City
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodNewsletter.xml",  # The New York Times - Food Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/TheEnd.xml",  # The New York Times - The End
    "https://rss.nytimes.com/services/xml/rss/nyt/Lens.xml",  # The New York Times - Lens
    "https://rss.nytimes.com/services/xml/rss/nyt/TomFriedman.xml",  # The New York Times - Tom Friedman
    "https://rss.nytimes.com/services/xml/rss/nyt/SiteMap.xml",  # The New York Times - Site Map
    "https://rss.nytimes.com/services/xml/rss/nyt/Columnist.xml",  # The New York Times - Columnist
    "https://rss.nytimes.com/services/xml/rss/nyt/DesignandLiving.xml",  # The New York Times - Design and Living
    "https://rss.nytimes.com/services/xml/rss/nyt/Environment.xml",  # The New York Times - Environment
    "https://rss.nytimes.com/services/xml/rss/nyt/SportsWeek.xml",  # The New York Times - Sports Week
    "https://rss.nytimes.com/services/xml/rss/nyt/Letter.xml",  # The New York Times - Letter
    "https://rss.nytimes.com/services/xml/rss/nyt/Live.xml",  # The New York Times - Live
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayBusiness.xml",  # The New York Times - Sunday Business
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayStyles.xml",  # The New York Times - Sunday Styles
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceTake.xml",  # The New York Times - ScienceTake
    "https://rss.nytimes.com/services/xml/rss/nyt/TheLivesTheyLived.xml",  # The New York Times - The Lives They Lived
    "https://rss.nytimes.com/services/xml/rss/nyt/WellFamily.xml",  # The New York Times - Well Family
    "https://rss.nytimes.com/services/xml/rss/nyt/MagazineEmail.xml",  # The New York Times - Magazine Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLove.xml",  # The New York Times - Modern Love
    "https://rss.nytimes.com/services/xml/rss/nyt/BooksEmail.xml",  # The New York Times - Books Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BookReview.xml",  # The New York Times - Book Review
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/FashionEmail.xml",  # The New York Times - Fashion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodEmail.xml",  # The New York Times - Food Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TravelEmail.xml",  # The New York Times - Travel Email
    "https://rss.nytimes.com/services/xml/rss/nyt/HomeEmail.xml",  # The New York Times - Home Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Crossword.xml",  # The New York Times - Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/RealEstateEmail.xml",  # The New York Times - Real Estate Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Games.xml",  # The New York Times - Games
    "https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",  # The New York Times - Personal Tech
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsletterToday.xml",  # The New York Times - Newsletter Today
    "https://rss.nytimes.com/services/xml/rss/nyt/NewslettersandAlerts.xml",  # The New York Times - Newsletters and Alerts
    "https://rss.nytimes.com/services/xml/rss/nyt/SpecialSections.xml",  # The New York Times - Special Sections
    "https://rss.nytimes.com/services/xml/rss/nyt/MobileApplications.xml",  # The New York Times - Mobile Applications
    "https://rss.nytimes.com/services/xml/rss/nyt/Video.xml",  # The New York Times - Video
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefing.xml",  # The New York Times - Daily Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeek.xml",  # The New York Times - The Week
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsEvent.xml",  # The New York Times - News Event
    "https://rss.nytimes.com/services/xml/rss/nyt/Audio.xml",  # The New York Times - Audio
    "https://rss.nytimes.com/services/xml/rss/nyt/MorningBriefing.xml",  # The New York Times - Morning Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/EveningBriefing.xml",  # The New York Times - Evening Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/MiniCrossword.xml",  # The New York Times - Mini Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/Opinion.xml",  # The New York Times - Opinion
    "https://rss.nytimes.com/services/xml/rss/nyt/ReaderCenterPodcasts.xml",  # The New York Times - Reader Center Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/FrontPage.xml",  # The New York Times - Front Page
    "https://rss.nytimes.com/services/xml/rss/nyt/BehindTheCover.xml",  # The New York Times - Behind The Cover
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekly.xml",  # The New York Times - The Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewPodcasts.xml",  # The New York Times - Sunday Review Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/WeekendRead.xml",  # The New York Times - Weekend Read
    "https://rss.nytimes.com/services/xml/rss/nyt/Privacy.xml",  # The New York Times - Privacy
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordEmail.xml",  # The New York Times - Crossword Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BusinessEmail.xml",  # The New York Times - Business Email
    "https://rss.nytimes.com/services/xml/rss/nyt/OpinionEmail.xml",  # The New York Times - Opinion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekEmail.xml",  # The New York Times - The Week Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail.xml",  # The New York Times - Science Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ForeignAffairs.xml",  # The New York Times - Foreign Affairs
    "https://rss.nytimes.com/services/xml/rss/nyt/Elections.xml",  # The New York Times - Elections
    "https://rss.nytimes.com/services/xml/rss/nyt/Postcards.xml",  # The New York Times - Postcards
    "https://rss.nytimes.com/services/xml/rss/nyt/Magazine.xml",  # The New York Times - Magazine
    "https://rss.nytimes.com/services/xml/rss/nyt/Parenting.xml",  # The New York Times - Parenting
    "https://rss.nytimes.com/services/xml/rss/nyt/HealthcareEmail.xml",  # The New York Times - Healthcare Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekender.xml",  # The New York Times - The Weekender
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/SmarterLivingEmail.xml",  # The New York Times - Smarter Living Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BestofLateNight.xml",  # The New York Times - Best of Late Night
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLovePodcast.xml",  # The New York Times - Modern Love Podcast
    "https://rss.nytimes.com/services/xml/rss/nyt/Heard.xml",  # The New York Times - Heard
    "https://rss.nytimes.com/services/xml/rss/nyt/Morning.xml",  # The New York Times - Morning
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayRead.xml",  # The New York Times - Sunday Read
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewEmail.xml",  # The New York Times - Sunday Review Email
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordExpress.xml",  # The New York Times - Crossword Express
    "https://rss.nytimes.com/services/xml/rss/nyt/Spirituality.xml",  # The New York Times - Spirituality
    "https://rss.nytimes.com/services/xml/rss/nyt/Champions.xml",  # The New York Times - Champions
    "https://rss.nytimes.com/services/xml/rss/nyt/Newsletter.xml",  # The New York Times - Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/InTheLoop.xml",  # The New York Times - In The Loop
    "https://rss.nytimes.com/services/xml/rss/nyt/Laurels.xml",  # The New York Times - Laurels
    "https://rss.nytimes.com/services/xml/rss/nyt/Working.xml",  # The New York Times - Working
    "https://rss.nytimes.com/services/xml/rss/nyt/Watching.xml",  # The New York Times - Watching
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/Wellness.xml",  # The New York Times - Wellness
    "https://rss.nytimes.com/services/xml/rss/nyt/ClimateHub.xml",  # The New York Times - Climate Hub
    "https://rss.nytimes.com/services/xml/rss/nyt/Podcasts.xml",  # The New York Times - Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/ReadersCenters.xml",  # The New York Times - Readers Centers
    "https://rss.nytimes.com/services/xml/rss/nyt/AtWar.xml",  # The New York Times - At War
    "https://rss.nytimes.com/services/xml/rss/nyt/RebeccaZamolo.xml",  # The New York Times - Rebecca Zamolo
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyNewsletter.xml",  # The New York Times - Daily Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/College.xml",  # The New York Times - College
    "https://rss.nytimes.com/services/xml/rss/nyt/Whistleblower.xml",  # The New York Times - Whistleblower
    "https://rss.nytimes.com/services/xml/rss/nyt/TheNewYorkTimes.xml",  # The New York Times - The New York Times
    "https://rss.nytimes.com/services/xml/rss/nyt/OnlineMarketplace.xml",  # The New York Times - Online Marketplace
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefings.xml",  # The New York Times - Daily Briefings
    "https://rss.nytimes.com/services/xml/rss/nyt/MyNewYork.xml",  # The New York Times - My New York
    "https://rss.nytimes.com/services/xml/rss/nyt/GlobalSports.xml",  # The New York Times - Global Sports
    "https://rss.nytimes.com/services/xml/rss/nyt/AboutOurAds.xml",  # The New York Times - About Our Ads
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordDaily.xml",  # The New York Times - Crossword Daily
    "https://rss.nytimes.com/services/xml/rss/nyt/Stop.xml",  # The New York Times - Stop
    "https://rss.nytimes.com/services/xml/rss/nyt/CaliforniaSunday.xml",  # The New York Times - California Sunday
    "https://rss.nytimes.com/services/xml/rss/nyt/NextDoor.xml",  # The New York Times - Next Door
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail2020.xml",  # The New York Times - Science Email 2020
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/BigCity.xml",  # The New York Times - Big City
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodNewsletter.xml",  # The New York Times - Food Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/TheEnd.xml",  # The New York Times - The End
    "https://rss.nytimes.com/services/xml/rss/nyt/Lens.xml",  # The New York Times - Lens
    "https://rss.nytimes.com/services/xml/rss/nyt/TomFriedman.xml",  # The New York Times - Tom Friedman
    "https://rss.nytimes.com/services/xml/rss/nyt/SiteMap.xml",  # The New York Times - Site Map
    "https://rss.nytimes.com/services/xml/rss/nyt/Columnist.xml",  # The New York Times - Columnist
    "https://rss.nytimes.com/services/xml/rss/nyt/DesignandLiving.xml",  # The New York Times - Design and Living
    "https://rss.nytimes.com/services/xml/rss/nyt/Environment.xml",  # The New York Times - Environment
    "https://rss.nytimes.com/services/xml/rss/nyt/SportsWeek.xml",  # The New York Times - Sports Week
    "https://rss.nytimes.com/services/xml/rss/nyt/Letter.xml",  # The New York Times - Letter
    "https://rss.nytimes.com/services/xml/rss/nyt/Live.xml",  # The New York Times - Live
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayBusiness.xml",  # The New York Times - Sunday Business
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayStyles.xml",  # The New York Times - Sunday Styles
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceTake.xml",  # The New York Times - ScienceTake
    "https://rss.nytimes.com/services/xml/rss/nyt/TheLivesTheyLived.xml",  # The New York Times - The Lives They Lived
    "https://rss.nytimes.com/services/xml/rss/nyt/WellFamily.xml",  # The New York Times - Well Family
    "https://rss.nytimes.com/services/xml/rss/nyt/MagazineEmail.xml",  # The New York Times - Magazine Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLove.xml",  # The New York Times - Modern Love
    "https://rss.nytimes.com/services/xml/rss/nyt/BooksEmail.xml",  # The New York Times - Books Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BookReview.xml",  # The New York Times - Book Review
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/FashionEmail.xml",  # The New York Times - Fashion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodEmail.xml",  # The New York Times - Food Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TravelEmail.xml",  # The New York Times - Travel Email
    "https://rss.nytimes.com/services/xml/rss/nyt/HomeEmail.xml",  # The New York Times - Home Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Crossword.xml",  # The New York Times - Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/RealEstateEmail.xml",  # The New York Times - Real Estate Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Games.xml",  # The New York Times - Games
    "https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",  # The New York Times - Personal Tech
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsletterToday.xml",  # The New York Times - Newsletter Today
    "https://rss.nytimes.com/services/xml/rss/nyt/NewslettersandAlerts.xml",  # The New York Times - Newsletters and Alerts
    "https://rss.nytimes.com/services/xml/rss/nyt/SpecialSections.xml",  # The New York Times - Special Sections
    "https://rss.nytimes.com/services/xml/rss/nyt/MobileApplications.xml",  # The New York Times - Mobile Applications
    "https://rss.nytimes.com/services/xml/rss/nyt/Video.xml",  # The New York Times - Video
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefing.xml",  # The New York Times - Daily Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeek.xml",  # The New York Times - The Week
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsEvent.xml",  # The New York Times - News Event
    "https://rss.nytimes.com/services/xml/rss/nyt/Audio.xml",  # The New York Times - Audio
    "https://rss.nytimes.com/services/xml/rss/nyt/MorningBriefing.xml",  # The New York Times - Morning Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/EveningBriefing.xml",  # The New York Times - Evening Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/MiniCrossword.xml",  # The New York Times - Mini Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/Opinion.xml",  # The New York Times - Opinion
    "https://rss.nytimes.com/services/xml/rss/nyt/ReaderCenterPodcasts.xml",  # The New York Times - Reader Center Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/FrontPage.xml",  # The New York Times - Front Page
    "https://rss.nytimes.com/services/xml/rss/nyt/BehindTheCover.xml",  # The New York Times - Behind The Cover
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekly.xml",  # The New York Times - The Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewPodcasts.xml",  # The New York Times - Sunday Review Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/WeekendRead.xml",  # The New York Times - Weekend Read
    "https://rss.nytimes.com/services/xml/rss/nyt/Privacy.xml",  # The New York Times - Privacy
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordEmail.xml",  # The New York Times - Crossword Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BusinessEmail.xml",  # The New York Times - Business Email
    "https://rss.nytimes.com/services/xml/rss/nyt/OpinionEmail.xml",  # The New York Times - Opinion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekEmail.xml",  # The New York Times - The Week Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail2020.xml",  # The New York Times - Science Email 2020
    "https://rss.nytimes.com/services/xml/rss/nyt/ForeignAffairs.xml",  # The New York Times - Foreign Affairs
    "https://rss.nytimes.com/services/xml/rss/nyt/Elections.xml",  # The New York Times - Elections
    "https://rss.nytimes.com/services/xml/rss/nyt/Postcards.xml",  # The New York Times - Postcards
    "https://rss.nytimes.com/services/xml/rss/nyt/Magazine.xml",  # The New York Times - Magazine
    "https://rss.nytimes.com/services/xml/rss/nyt/Parenting.xml",  # The New York Times - Parenting
    "https://rss.nytimes.com/services/xml/rss/nyt/HealthcareEmail.xml",  # The New York Times - Healthcare Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekender.xml",  # The New York Times - The Weekender
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/SmarterLivingEmail.xml",  # The New York Times - Smarter Living Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BestofLateNight.xml",  # The New York Times - Best of Late Night
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLovePodcast.xml",  # The New York Times - Modern Love Podcast
    "https://rss.nytimes.com/services/xml/rss/nyt/Heard.xml",  # The New York Times - Heard
    "https://rss.nytimes.com/services/xml/rss/nyt/Morning.xml",  # The New York Times - Morning
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayRead.xml",  # The New York Times - Sunday Read
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewEmail.xml",  # The New York Times - Sunday Review Email
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordExpress.xml",  # The New York Times - Crossword Express
    "https://rss.nytimes.com/services/xml/rss/nyt/Spirituality.xml",  # The New York Times - Spirituality
    "https://rss.nytimes.com/services/xml/rss/nyt/Champions.xml",  # The New York Times - Champions
    "https://rss.nytimes.com/services/xml/rss/nyt/Newsletter.xml",  # The New York Times - Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/InTheLoop.xml",  # The New York Times - In The Loop
    "https://rss.nytimes.com/services/xml/rss/nyt/Laurels.xml",  # The New York Times - Laurels
    "https://rss.nytimes.com/services/xml/rss/nyt/Working.xml",  # The New York Times - Working
    "https://rss.nytimes.com/services/xml/rss/nyt/Watching.xml",  # The New York Times - Watching
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/Wellness.xml",  # The New York Times - Wellness
    "https://rss.nytimes.com/services/xml/rss/nyt/ClimateHub.xml",  # The New York Times - Climate Hub
    "https://rss.nytimes.com/services/xml/rss/nyt/Podcasts.xml",  # The New York Times - Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/ReadersCenters.xml",  # The New York Times - Readers Centers
    "https://rss.nytimes.com/services/xml/rss/nyt/AtWar.xml",  # The New York Times - At War
    "https://rss.nytimes.com/services/xml/rss/nyt/RebeccaZamolo.xml",  # The New York Times - Rebecca Zamolo
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyNewsletter.xml",  # The New York Times - Daily Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/College.xml",  # The New York Times - College
    "https://rss.nytimes.com/services/xml/rss/nyt/Whistleblower.xml",  # The New York Times - Whistleblower
    "https://rss.nytimes.com/services/xml/rss/nyt/TheNewYorkTimes.xml",  # The New York Times - The New York Times
    "https://rss.nytimes.com/services/xml/rss/nyt/OnlineMarketplace.xml",  # The New York Times - Online Marketplace
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefings.xml",  # The New York Times - Daily Briefings
    "https://rss.nytimes.com/services/xml/rss/nyt/MyNewYork.xml",  # The New York Times - My New York
    "https://rss.nytimes.com/services/xml/rss/nyt/GlobalSports.xml",  # The New York Times - Global Sports
    "https://rss.nytimes.com/services/xml/rss/nyt/AboutOurAds.xml",  # The New York Times - About Our Ads
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordDaily.xml",  # The New York Times - Crossword Daily
    "https://rss.nytimes.com/services/xml/rss/nyt/Stop.xml",  # The New York Times - Stop
    "https://rss.nytimes.com/services/xml/rss/nyt/CaliforniaSunday.xml",  # The New York Times - California Sunday
    "https://rss.nytimes.com/services/xml/rss/nyt/NextDoor.xml",  # The New York Times - Next Door
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail2020.xml",  # The New York Times - Science Email 2020
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/BigCity.xml",  # The New York Times - Big City
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodNewsletter.xml",  # The New York Times - Food Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/TheEnd.xml",  # The New York Times - The End
    "https://rss.nytimes.com/services/xml/rss/nyt/Lens.xml",  # The New York Times - Lens
    "https://rss.nytimes.com/services/xml/rss/nyt/TomFriedman.xml",  # The New York Times - Tom Friedman
    "https://rss.nytimes.com/services/xml/rss/nyt/SiteMap.xml",  # The New York Times - Site Map
    "https://rss.nytimes.com/services/xml/rss/nyt/Columnist.xml",  # The New York Times - Columnist
    "https://rss.nytimes.com/services/xml/rss/nyt/DesignandLiving.xml",  # The New York Times - Design and Living
    "https://rss.nytimes.com/services/xml/rss/nyt/Environment.xml",  # The New York Times - Environment
    "https://rss.nytimes.com/services/xml/rss/nyt/SportsWeek.xml",  # The New York Times - Sports Week
    "https://rss.nytimes.com/services/xml/rss/nyt/Letter.xml",  # The New York Times - Letter
    "https://rss.nytimes.com/services/xml/rss/nyt/Live.xml",  # The New York Times - Live
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayBusiness.xml",  # The New York Times - Sunday Business
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayStyles.xml",  # The New York Times - Sunday Styles
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceTake.xml",  # The New York Times - ScienceTake
    "https://rss.nytimes.com/services/xml/rss/nyt/TheLivesTheyLived.xml",  # The New York Times - The Lives They Lived
    "https://rss.nytimes.com/services/xml/rss/nyt/WellFamily.xml",  # The New York Times - Well Family
    "https://rss.nytimes.com/services/xml/rss/nyt/MagazineEmail.xml",  # The New York Times - Magazine Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLove.xml",  # The New York Times - Modern Love
    "https://rss.nytimes.com/services/xml/rss/nyt/BooksEmail.xml",  # The New York Times - Books Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BookReview.xml",  # The New York Times - Book Review
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/FashionEmail.xml",  # The New York Times - Fashion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodEmail.xml",  # The New York Times - Food Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TravelEmail.xml",  # The New York Times - Travel Email
    "https://rss.nytimes.com/services/xml/rss/nyt/HomeEmail.xml",  # The New York Times - Home Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Crossword.xml",  # The New York Times - Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/RealEstateEmail.xml",  # The New York Times - Real Estate Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Games.xml",  # The New York Times - Games
    "https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",  # The New York Times - Personal Tech
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsletterToday.xml",  # The New York Times - Newsletter Today
    "https://rss.nytimes.com/services/xml/rss/nyt/NewslettersandAlerts.xml",  # The New York Times - Newsletters and Alerts
    "https://rss.nytimes.com/services/xml/rss/nyt/SpecialSections.xml",  # The New York Times - Special Sections
    "https://rss.nytimes.com/services/xml/rss/nyt/MobileApplications.xml",  # The New York Times - Mobile Applications
    "https://rss.nytimes.com/services/xml/rss/nyt/Video.xml",  # The New York Times - Video
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefing.xml",  # The New York Times - Daily Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeek.xml",  # The New York Times - The Week
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsEvent.xml",  # The New York Times - News Event
    "https://rss.nytimes.com/services/xml/rss/nyt/Audio.xml",  # The New York Times - Audio
    "https://rss.nytimes.com/services/xml/rss/nyt/MorningBriefing.xml",  # The New York Times - Morning Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/EveningBriefing.xml",  # The New York Times - Evening Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/MiniCrossword.xml",  # The New York Times - Mini Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/Opinion.xml",  # The New York Times - Opinion
    "https://rss.nytimes.com/services/xml/rss/nyt/ReaderCenterPodcasts.xml",  # The New York Times - Reader Center Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/FrontPage.xml",  # The New York Times - Front Page
    "https://rss.nytimes.com/services/xml/rss/nyt/BehindTheCover.xml",  # The New York Times - Behind The Cover
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekly.xml",  # The New York Times - The Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewPodcasts.xml",  # The New York Times - Sunday Review Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/WeekendRead.xml",  # The New York Times - Weekend Read
    "https://rss.nytimes.com/services/xml/rss/nyt/Privacy.xml",  # The New York Times - Privacy
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordEmail.xml",  # The New York Times - Crossword Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BusinessEmail.xml",  # The New York Times - Business Email
    "https://rss.nytimes.com/services/xml/rss/nyt/OpinionEmail.xml",  # The New York Times - Opinion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekEmail.xml",  # The New York Times - The Week Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail.xml",  # The New York Times - Science Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ForeignAffairs.xml",  # The New York Times - Foreign Affairs
    "https://rss.nytimes.com/services/xml/rss/nyt/Elections.xml",  # The New York Times - Elections
    "https://rss.nytimes.com/services/xml/rss/nyt/Postcards.xml",  # The New York Times - Postcards
    "https://rss.nytimes.com/services/xml/rss/nyt/Magazine.xml",  # The New York Times - Magazine
    "https://rss.nytimes.com/services/xml/rss/nyt/Parenting.xml",  # The New York Times - Parenting
    "https://rss.nytimes.com/services/xml/rss/nyt/HealthcareEmail.xml",  # The New York Times - Healthcare Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekender.xml",  # The New York Times - The Weekender
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/SmarterLivingEmail.xml",  # The New York Times - Smarter Living Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BestofLateNight.xml",  # The New York Times - Best of Late Night
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLovePodcast.xml",  # The New York Times - Modern Love Podcast
    "https://rss.nytimes.com/services/xml/rss/nyt/Heard.xml",  # The New York Times - Heard
    "https://rss.nytimes.com/services/xml/rss/nyt/Morning.xml",  # The New York Times - Morning
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayRead.xml",  # The New York Times - Sunday Read
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewEmail.xml",  # The New York Times - Sunday Review Email
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordExpress.xml",  # The New York Times - Crossword Express
    "https://rss.nytimes.com/services/xml/rss/nyt/Spirituality.xml",  # The New York Times - Spirituality
    "https://rss.nytimes.com/services/xml/rss/nyt/Champions.xml",  # The New York Times - Champions
    "https://rss.nytimes.com/services/xml/rss/nyt/Newsletter.xml",  # The New York Times - Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/InTheLoop.xml",  # The New York Times - In The Loop
    "https://rss.nytimes.com/services/xml/rss/nyt/Laurels.xml",  # The New York Times - Laurels
    "https://rss.nytimes.com/services/xml/rss/nyt/Working.xml",  # The New York Times - Working
    "https://rss.nytimes.com/services/xml/rss/nyt/Watching.xml",  # The New York Times - Watching
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/Wellness.xml",  # The New York Times - Wellness
    "https://rss.nytimes.com/services/xml/rss/nyt/ClimateHub.xml",  # The New York Times - Climate Hub
    "https://rss.nytimes.com/services/xml/rss/nyt/Podcasts.xml",  # The New York Times - Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/ReadersCenters.xml",  # The New York Times - Readers Centers
    "https://rss.nytimes.com/services/xml/rss/nyt/AtWar.xml",  # The New York Times - At War
    "https://rss.nytimes.com/services/xml/rss/nyt/RebeccaZamolo.xml",  # The New York Times - Rebecca Zamolo
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyNewsletter.xml",  # The New York Times - Daily Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/College.xml",  # The New York Times - College
    "https://rss.nytimes.com/services/xml/rss/nyt/Whistleblower.xml",  # The New York Times - Whistleblower
    "https://rss.nytimes.com/services/xml/rss/nyt/TheNewYorkTimes.xml",  # The New York Times - The New York Times
    "https://rss.nytimes.com/services/xml/rss/nyt/OnlineMarketplace.xml",  # The New York Times - Online Marketplace
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefings.xml",  # The New York Times - Daily Briefings
    "https://rss.nytimes.com/services/xml/rss/nyt/MyNewYork.xml",  # The New York Times - My New York
    "https://rss.nytimes.com/services/xml/rss/nyt/GlobalSports.xml",  # The New York Times - Global Sports
    "https://rss.nytimes.com/services/xml/rss/nyt/AboutOurAds.xml",  # The New York Times - About Our Ads
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordDaily.xml",  # The New York Times - Crossword Daily
    "https://rss.nytimes.com/services/xml/rss/nyt/Stop.xml",  # The New York Times - Stop
    "https://rss.nytimes.com/services/xml/rss/nyt/CaliforniaSunday.xml",  # The New York Times - California Sunday
    "https://rss.nytimes.com/services/xml/rss/nyt/NextDoor.xml",  # The New York Times - Next Door
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail2020.xml",  # The New York Times - Science Email 2020
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/BigCity.xml",  # The New York Times - Big City
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodNewsletter.xml",  # The New York Times - Food Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/TheEnd.xml",  # The New York Times - The End
    "https://rss.nytimes.com/services/xml/rss/nyt/Lens.xml",  # The New York Times - Lens
    "https://rss.nytimes.com/services/xml/rss/nyt/TomFriedman.xml",  # The New York Times - Tom Friedman
    "https://rss.nytimes.com/services/xml/rss/nyt/SiteMap.xml",  # The New York Times - Site Map
    "https://rss.nytimes.com/services/xml/rss/nyt/Columnist.xml",  # The New York Times - Columnist
    "https://rss.nytimes.com/services/xml/rss/nyt/DesignandLiving.xml",  # The New York Times - Design and Living
    "https://rss.nytimes.com/services/xml/rss/nyt/Environment.xml",  # The New York Times - Environment
    "https://rss.nytimes.com/services/xml/rss/nyt/SportsWeek.xml",  # The New York Times - Sports Week
    "https://rss.nytimes.com/services/xml/rss/nyt/Letter.xml",  # The New York Times - Letter
    "https://rss.nytimes.com/services/xml/rss/nyt/Live.xml",  # The New York Times - Live
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayBusiness.xml",  # The New York Times - Sunday Business
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayStyles.xml",  # The New York Times - Sunday Styles
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceTake.xml",  # The New York Times - ScienceTake
    "https://rss.nytimes.com/services/xml/rss/nyt/TheLivesTheyLived.xml",  # The New York Times - The Lives They Lived
    "https://rss.nytimes.com/services/xml/rss/nyt/WellFamily.xml",  # The New York Times - Well Family
    "https://rss.nytimes.com/services/xml/rss/nyt/MagazineEmail.xml",  # The New York Times - Magazine Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLove.xml",  # The New York Times - Modern Love
    "https://rss.nytimes.com/services/xml/rss/nyt/BooksEmail.xml",  # The New York Times - Books Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BookReview.xml",  # The New York Times - Book Review
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/FashionEmail.xml",  # The New York Times - Fashion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodEmail.xml",  # The New York Times - Food Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TravelEmail.xml",  # The New York Times - Travel Email
    "https://rss.nytimes.com/services/xml/rss/nyt/HomeEmail.xml",  # The New York Times - Home Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Crossword.xml",  # The New York Times - Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/RealEstateEmail.xml",  # The New York Times - Real Estate Email
    "https://rss.nytimes.com/services/xml/rss/nyt/Games.xml",  # The New York Times - Games
    "https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",  # The New York Times - Personal Tech
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsletterToday.xml",  # The New York Times - Newsletter Today
    "https://rss.nytimes.com/services/xml/rss/nyt/NewslettersandAlerts.xml",  # The New York Times - Newsletters and Alerts
    "https://rss.nytimes.com/services/xml/rss/nyt/SpecialSections.xml",  # The New York Times - Special Sections
    "https://rss.nytimes.com/services/xml/rss/nyt/MobileApplications.xml",  # The New York Times - Mobile Applications
    "https://rss.nytimes.com/services/xml/rss/nyt/Video.xml",  # The New York Times - Video
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefing.xml",  # The New York Times - Daily Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeek.xml",  # The New York Times - The Week
    "https://rss.nytimes.com/services/xml/rss/nyt/NewsEvent.xml",  # The New York Times - News Event
    "https://rss.nytimes.com/services/xml/rss/nyt/Audio.xml",  # The New York Times - Audio
    "https://rss.nytimes.com/services/xml/rss/nyt/MorningBriefing.xml",  # The New York Times - Morning Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/EveningBriefing.xml",  # The New York Times - Evening Briefing
    "https://rss.nytimes.com/services/xml/rss/nyt/MiniCrossword.xml",  # The New York Times - Mini Crossword
    "https://rss.nytimes.com/services/xml/rss/nyt/Opinion.xml",  # The New York Times - Opinion
    "https://rss.nytimes.com/services/xml/rss/nyt/ReaderCenterPodcasts.xml",  # The New York Times - Reader Center Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/FrontPage.xml",  # The New York Times - Front Page
    "https://rss.nytimes.com/services/xml/rss/nyt/BehindTheCover.xml",  # The New York Times - Behind The Cover
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekly.xml",  # The New York Times - The Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewPodcasts.xml",  # The New York Times - Sunday Review Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/WeekendRead.xml",  # The New York Times - Weekend Read
    "https://rss.nytimes.com/services/xml/rss/nyt/Privacy.xml",  # The New York Times - Privacy
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordEmail.xml",  # The New York Times - Crossword Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BusinessEmail.xml",  # The New York Times - Business Email
    "https://rss.nytimes.com/services/xml/rss/nyt/OpinionEmail.xml",  # The New York Times - Opinion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekEmail.xml",  # The New York Times - The Week Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail.xml",  # The New York Times - Science Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ForeignAffairs.xml",  # The New York Times - Foreign Affairs
    "https://rss.nytimes.com/services/xml/rss/nyt/Elections.xml",  # The New York Times - Elections
    "https://rss.nytimes.com/services/xml/rss/nyt/Postcards.xml",  # The New York Times - Postcards
    "https://rss.nytimes.com/services/xml/rss/nyt/Magazine.xml",  # The New York Times - Magazine
    "https://rss.nytimes.com/services/xml/rss/nyt/Parenting.xml",  # The New York Times - Parenting
    "https://rss.nytimes.com/services/xml/rss/nyt/HealthcareEmail.xml",  # The New York Times - Healthcare Email
    "https://rss.nytimes.com/services/xml/rss/nyt/TheWeekender.xml",  # The New York Times - The Weekender
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/SmarterLivingEmail.xml",  # The New York Times - Smarter Living Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BestofLateNight.xml",  # The New York Times - Best of Late Night
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLovePodcast.xml",  # The New York Times - Modern Love Podcast
    "https://rss.nytimes.com/services/xml/rss/nyt/Heard.xml",  # The New York Times - Heard
    "https://rss.nytimes.com/services/xml/rss/nyt/Morning.xml",  # The New York Times - Morning
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayRead.xml",  # The New York Times - Sunday Read
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayReviewEmail.xml",  # The New York Times - Sunday Review Email
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordExpress.xml",  # The New York Times - Crossword Express
    "https://rss.nytimes.com/services/xml/rss/nyt/Spirituality.xml",  # The New York Times - Spirituality
    "https://rss.nytimes.com/services/xml/rss/nyt/Champions.xml",  # The New York Times - Champions
    "https://rss.nytimes.com/services/xml/rss/nyt/Newsletter.xml",  # The New York Times - Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/InTheLoop.xml",  # The New York Times - In The Loop
    "https://rss.nytimes.com/services/xml/rss/nyt/Laurels.xml",  # The New York Times - Laurels
    "https://rss.nytimes.com/services/xml/rss/nyt/Working.xml",  # The New York Times - Working
    "https://rss.nytimes.com/services/xml/rss/nyt/Watching.xml",  # The New York Times - Watching
    "https://rss.nytimes.com/services/xml/rss/nyt/SpokenEdition.xml",  # The New York Times - Spoken Edition
    "https://rss.nytimes.com/services/xml/rss/nyt/Wellness.xml",  # The New York Times - Wellness
    "https://rss.nytimes.com/services/xml/rss/nyt/ClimateHub.xml",  # The New York Times - Climate Hub
    "https://rss.nytimes.com/services/xml/rss/nyt/Podcasts.xml",  # The New York Times - Podcasts
    "https://rss.nytimes.com/services/xml/rss/nyt/ReadersCenters.xml",  # The New York Times - Readers Centers
    "https://rss.nytimes.com/services/xml/rss/nyt/AtWar.xml",  # The New York Times - At War
    "https://rss.nytimes.com/services/xml/rss/nyt/RebeccaZamolo.xml",  # The New York Times - Rebecca Zamolo
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyNewsletter.xml",  # The New York Times - Daily Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/College.xml",  # The New York Times - College
    "https://rss.nytimes.com/services/xml/rss/nyt/Whistleblower.xml",  # The New York Times - Whistleblower
    "https://rss.nytimes.com/services/xml/rss/nyt/TheNewYorkTimes.xml",  # The New York Times - The New York Times
    "https://rss.nytimes.com/services/xml/rss/nyt/OnlineMarketplace.xml",  # The New York Times - Online Marketplace
    "https://rss.nytimes.com/services/xml/rss/nyt/DailyBriefings.xml",  # The New York Times - Daily Briefings
    "https://rss.nytimes.com/services/xml/rss/nyt/MyNewYork.xml",  # The New York Times - My New York
    "https://rss.nytimes.com/services/xml/rss/nyt/GlobalSports.xml",  # The New York Times - Global Sports
    "https://rss.nytimes.com/services/xml/rss/nyt/AboutOurAds.xml",  # The New York Times - About Our Ads
    "https://rss.nytimes.com/services/xml/rss/nyt/CrosswordDaily.xml",  # The New York Times - Crossword Daily
    "https://rss.nytimes.com/services/xml/rss/nyt/Stop.xml",  # The New York Times - Stop
    "https://rss.nytimes.com/services/xml/rss/nyt/CaliforniaSunday.xml",  # The New York Times - California Sunday
    "https://rss.nytimes.com/services/xml/rss/nyt/NextDoor.xml",  # The New York Times - Next Door
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceEmail2020.xml",  # The New York Times - Science Email 2020
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/BigCity.xml",  # The New York Times - Big City
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodNewsletter.xml",  # The New York Times - Food Newsletter
    "https://rss.nytimes.com/services/xml/rss/nyt/TheEnd.xml",  # The New York Times - The End
    "https://rss.nytimes.com/services/xml/rss/nyt/Lens.xml",  # The New York Times - Lens
    "https://rss.nytimes.com/services/xml/rss/nyt/TomFriedman.xml",  # The New York Times - Tom Friedman
    "https://rss.nytimes.com/services/xml/rss/nyt/SiteMap.xml",  # The New York Times - Site Map
    "https://rss.nytimes.com/services/xml/rss/nyt/Columnist.xml",  # The New York Times - Columnist
    "https://rss.nytimes.com/services/xml/rss/nyt/DesignandLiving.xml",  # The New York Times - Design and Living
    "https://rss.nytimes.com/services/xml/rss/nyt/Environment.xml",  # The New York Times - Environment
    "https://rss.nytimes.com/services/xml/rss/nyt/SportsWeek.xml",  # The New York Times - Sports Week
    "https://rss.nytimes.com/services/xml/rss/nyt/Letter.xml",  # The New York Times - Letter
    "https://rss.nytimes.com/services/xml/rss/nyt/Live.xml",  # The New York Times - Live
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayBusiness.xml",  # The New York Times - Sunday Business
    "https://rss.nytimes.com/services/xml/rss/nyt/SundayStyles.xml",  # The New York Times - Sunday Styles
    "https://rss.nytimes.com/services/xml/rss/nyt/ScienceTake.xml",  # The New York Times - ScienceTake
    "https://rss.nytimes.com/services/xml/rss/nyt/TheLivesTheyLived.xml",  # The New York Times - The Lives They Lived
    "https://rss.nytimes.com/services/xml/rss/nyt/WellFamily.xml",  # The New York Times - Well Family
    "https://rss.nytimes.com/services/xml/rss/nyt/MagazineEmail.xml",  # The New York Times - Magazine Email
    "https://rss.nytimes.com/services/xml/rss/nyt/ModernLove.xml",  # The New York Times - Modern Love
    "https://rss.nytimes.com/services/xml/rss/nyt/BooksEmail.xml",  # The New York Times - Books Email
    "https://rss.nytimes.com/services/xml/rss/nyt/BookReview.xml",  # The New York Times - Book Review
    "https://rss.nytimes.com/services/xml/rss/nyt/InternationalWeekly.xml",  # The New York Times - International Weekly
    "https://rss.nytimes.com/services/xml/rss/nyt/FashionEmail.xml",  # The New York Times - Fashion Email
    "https://rss.nytimes.com/services/xml/rss/nyt/FoodEmail.xml",  # The New York Times - Food Email
    "http://feeds.bbci.co.uk/news/rss.xml",  # BBC News
    "http://feeds.reuters.com/reuters/topNews",  # Reuters - Top News
    "https://news.ycombinator.com/rss",  # Hacker News
    "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss",  # NASA News
    "https://www.espn.com/espn/rss/news",  # ESPN - Top Headlines
    "http://feeds.feedburner.com/TechCrunch",  # TechCrunch
    "https://www.theguardian.com/world/rss",  # The Guardian - World News
    "https://feeds.npr.org/1001/rss.xml",  # NPR - Top Stories
    "https://www.aljazeera.com/xml/rss/all.xml",  # Al Jazeera
    "https://www.dw.com/feeds/12014/rss.xml",  # DW News
    "http://feeds.feedburner.com/time/topstories",  # TIME - Top Stories
    "https://www.abc.net.au/news/feed/51120/rss.xml",  # ABC News (Australia)
    "https://www.nbcnews.com/id/3032091/device/rss/rss.xml",  # NBC News
    "https://www.cnn.com/rss/cnn_topstories.rss",  # CNN - Top Stories
    "http://rss.cbc.ca/lineup/topstories.xml",  # CBC News
    "http://feeds.skynews.com/feeds/rss/home.xml",  # Sky News
    "https://rss.sciencedaily.com/top.xml",  # ScienceDaily - Top Science News
    "https://www.economist.com/latest/rss.xml",  # The Economist
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",  # Times of India
    "https://feeds.bbci.co.uk/sport/rss.xml",  # BBC Sport
    "https://www.techradar.com/rss",  # TechRadar
    "http://feeds.feedburner.com/IGNPS4All",  # IGN - PlayStation News
    "https://lifehacker.com/rss",  # Lifehacker
    "https://feeds.feedburner.com/TechCrunch/gaming",  # TechCrunch - Gaming
    "https://www.nintendolife.com/feeds/latest",  # Nintendo Life
    "https://www.recode.net/rss/index.xml",  # Recode
    "http://feeds.feedburner.com/TheHackersNews",  # The Hacker News
    "https://www.reddit.com/r/programming/.rss",  # Reddit /r/programming
    "https://www.reddit.com/r/worldnews/.rss",  # Reddit /r/worldnews
    "https://feeds.feedburner.com/blogspot/hsDu",  # A List Apart - Web Design
    "https://www.androidcentral.com/rss.xml",  # Android Central
    "https://www.macrumors.com/mac/iphone/rss/",  # MacRumors - iPhone
    "https://www.windowscentral.com/rss.xml",  # Windows Central
    "https://www.reddit.com/r/science/.rss",  # Reddit /r/science
    "https://www.reddit.com/r/technology/.rss",  # Reddit /r/technology
    "https://www.theverge.com/rss/index.xml",  # The Verge
    "https://arstechnica.com/feed/",  # Ars Technica
    "https://www.buzzfeed.com/world.xml",  # BuzzFeed News - World
    "https://www.cbsnews.com/latest/rss/main",  # CBS News
    "https://www.dailytech.com/newsrss.xml",  # DailyTech
    "https://www.digitaltrends.com/feed/",  # Digital Trends
    "https://gizmodo.com/rss",  # Gizmodo
    "https://www.huffpost.com/section/front-page/feed",  # HuffPost
    "https://www.theatlantic.com/feed/all/",  # The Atlantic
    "https://www.vox.com/rss/index.xml",  # Vox
    "https://www.bbc.co.uk/sport/0/rss.xml",  # BBC Sport
    "https://www.sciencenews.org/feed",  # Science News
    "https://www.nationalgeographic.com/rss/latest.rss",  # National Geographic
    "https://www.businessinsider.com/sai/rss",  # Business Insider - Science
    "https://www.engadget.com/rss.xml",  # Engadget
    "https://www.popsci.com/rss.xml",  # Popular Science
    "https://www.space.com/feeds/all",  # Space.com
    "https://www.sportsnet.ca/feed/",  # Sportsnet
    "https://www.thedailybeast.com/rss",  # The Daily Beast
    "https://www.vanityfair.com/feed/rss",  # Vanity Fair
    "https://www.wired.com/feed/rss",  # WIRED
    "https://www.gamasutra.com/rss.xml",  # Gamasutra
    "https://kotaku.com/rss",  # Kotaku
    "https://www.boston.com/tag/sports/rss",  # Boston.com Sports
    "https://www.cnet.com/rss/news/",  # CNET News
    "https://feeds.feedburner.com/SmallBusinessTrends",  # Small Business Trends
    "https://www.eonline.com/de/rss/news",  # E! News
    "https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/health/rss.xml",  # NY Times - Health
    # Technology and Science
    "https://www.androidcentral.com/rss.xml",
    "https://www.macrumors.com/mac/iphone/rss/",
    "https://www.windowscentral.com/rss.xml",
    "https://www.reddit.com/r/science/.rss",
    "https://www.reddit.com/r/technology/.rss",
    "https://www.theverge.com/rss/index.xml",
    "https://arstechnica.com/feed/",
    "https://www.dailytech.com/newsrss.xml",
    "https://www.digitaltrends.com/feed/",
    "https://gizmodo.com/rss",
    "https://www.popsci.com/rss.xml",
    "https://www.sciencenews.org/feed",
    "https://www.space.com/feeds/all",
    "https://www.wired.com/feed/rss",
    "https://www.nationalgeographic.com/rss/latest.rss",
    "https://www.businessinsider.com/sai/rss",
    "https://www.engadget.com/rss.xml",
    "https://kotaku.com/rss",
    "https://www.cnet.com/rss/news/",

    # News and Current Affairs
    "https://www.bbc.co.uk/news/rss.xml",
    "https://www.cbsnews.com/latest/rss/main",
    "https://www.theguardian.com/world/rss",
    "https://abcnews.go.com/abcnews/topstories",
    "https://www.reuters.com/tools/rss",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://www.independent.co.uk/news/world/rss",
    "https://www.washingtonpost.com/wp-dyn/rss/national/index.xml",
    "https://www.huffpost.com/section/front-page/feed",
    "https://www.npr.org/rss/rss.php?id=1001",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://feeds.bbci.co.uk/news/technology/rss.xml",

    # Sports
    "https://www.espn.com/espn/rss/news",
    "https://www.sportingnews.com/us/rss",
    "https://www.bbc.co.uk/sport/0/rss.xml",
    "https://www.sportsnet.ca/feed/",

    # Entertainment
    "https://www.eonline.com/de/rss/news",
    "https://www.etonline.com/rss",
    "https://www.vanityfair.com/feed/rss",
    "https://www.hollywoodreporter.com/taxonomy/term/6/feed",
    "https://www.vulture.com/rss/all.xml",
    "https://www.buzzfeed.com/entertainment.xml",

    # Business and Finance
    "https://www.businessinsider.com/sai/rss",
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "https://www.wsj.com/xml/rss/3_7014.xml",
    "https://www.forbes.com/investing/feed2/",
    "https://www.fool.com/feeds/index.aspx",

    # Health and Wellness
    "https://www.webmd.com/rss/breaking-news.xml",
    "https://www.everydayhealth.com/feed-items.rss",
    "https://www.nhs.uk/conditions/rss",
    "https://www.healthline.com/rss/news",
    "https://www.mayoclinic.org/rss/news",
    "https://rss.nytimes.com/services/xml/rss/nyt/Health.xml",

    # Gaming
    "https://www.polygon.com/rss/index.xml",
    "https://www.gamasutra.com/rss.xml",
    "https://www.gamespot.com/feeds/mashup/",
    "https://www.ign.com/rss.xml",

    # Food and Cooking
    "https://www.foodnetwork.com/rss/newsletter.rss",
    "https://www.allrecipes.com/feed/",
    "https://www.bonappetit.com/feed/rss",
    "https://www.epicurious.com/services/rss/recipes",
    "https://www.simplyrecipes.com/feed/",
]
