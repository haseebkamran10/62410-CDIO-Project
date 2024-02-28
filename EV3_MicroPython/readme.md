

GolfBot-Prototype
Prækvalifikationsrunde og konkurrence
Indledning
Vores firma vil gerne markedsføre et system, GolfBot, der kan indsamle golfbolde fra en driving range. Vi mangler en partner i form af et udviklingshus, der kan hjælpe os med at udvikle hardware og software til GolfBot.
Prækvalifikation - Konkurrence
For at finde den rette partner har vi besluttet os for at gennemføre en prækvalifikationsrunde, hvor lovende virksomheder kan demonstrere at de besidder de nødvendige færdigheder til at udvikle et autonomt golfbold-indsamlingssystem. 

Den virksomhed (gruppe), der demonstrerer den prototype, der leverer den mest overbevisende præstation i prækvalifikationsrunden får, foruden kontrakten på hovedentreprisen, en præmie som anerkendelse for den præstation de har ydet. Vinderen af prækvalifikationsrunden vil blive fundet ved en konkurrence mod de andre deltagere på afslutningsdagen for projektet.

Som prækvalifikations-opgave har vi valgt en simplere udgave af hoved-problemstillingen, der dog indeholder mange af de samme elementer, som kendetegner det originale problem.
Vision
Da vi ikke kan have mennesker på driving rangen, mens der spilles golf, skal robotten fungere fuldstændigt autonomt. Efter igangsætning skal robotten kunne klare sig selv til opgaven er løst.

Robotten skal kunne klare at indsamle flest mulige bolde på kortest mulig tid, uden at ødelægge banens opsætning. Vi anvender bordtennis bolde som substitut for golf-bolde, da de kræver mindre solidt byggede robot-prototyper. Der vil desuden ikke blive skudt med bolde under indsamlingen, selvom det forventes at GolfBot skal kunne klare sig under beskydning på golfbanen i den endelige udgave.

I stedet for en driving range anvendes et afgrænset område på ca. 180 x 120 cm med en velkendt forhindring placeret på banen. 

Robotten skal indsamle og aflevere boldene i en beholder - i opgaven defineret ved et af to mål på banen. Det ene mål er mindre end det andet og det vil give flere points at aflevere boldene her. 

Der gives desuden point for antallet af indsamlede bolde, og lykkes det at indsamle alle bolde, gives der også points for resterende sekunder. I alt har man 8 minutter til at indsamle boldene. Der vil være 10 bolde på banen. Det vil være muligt at opsætte og kalibrere systemet inden start på indsamling. 

Det vil give minus-points at berøre banens kanter. Robotten placeres et valgfrit sted på banen af konstruktørerne. Banen og boldene må kun berøres af robotten (men ikke ved placering af robotten). 

Banen ser ud som illustreret nedenfor.


Banens kanter er 75 mm høje og målene er 45 mm høje. Målene er ca. mål og tegningen er ikke målfast. Krydset står ikke nødvendigvis orienteret som på tegningen og kan ligge op til 10 cm fra centrum af banen.

Point gives som følger: 

100 point pr bold der forlader banen gennem mål B
150 point pr. bold der forlader banen gennem mål A
3 point pr. resterende sekund når boldene er afleveret. 
-50 point hvis robotten berører banen/forhindringerne.
-100 hvis robotten flytter forhindringen/banen over 1 cm.

Det er tilladt at berøre/genstarte robotten inden for 8 minutter, men alle indsamlede bolde skal tilbagelægges tilfældigt på banen i givet fald og points for disse nulstilles. Strafpoints nulstilles ikke. En dommer tilbagelægger boldene.

Konkurrencekørslen skal optages af konstruktørerne med et separat kamera (eks. en mobiltelefon) som dokumentation af kørslen.

For at lette konkurrenternes udgifter udleveres til konstruktion af prototypen: 
Et sæt Lego Mindstorm Ev3.
Et flash kort, der passer i en Lego Mindstorm Controller.
Et kamerastativ.
Et USB kamera.
Resume
Udtænk, Design, Implementér og Operér et system, der autonomt kan indsamle bordtennisbolde på tid på en foruddefineret bane. 
Der vil være en konkurrence i slutningen af 3 ugers perioden. 
Vinderen bliver præmieret.

our repository structure 
LegoMindstormsGolf/
│
├── README.md               # Project overview and setup instructions
├── requirements.txt       # Python dependencies to install, if any
│
├── src/                   # Source code for the project
│   ├── main.py            # Main script to run the project
│   ├── mindstorms_control/ # LEGO Mindstorms control algorithms
│   │   ├── __init__.py
│   │   └── motor_control.py # Control motors, read sensors, etc.
│   │
│   ├── vision/            # Vision processing for the robot
│   │   ├── __init__.py
│   │   ├── camera_control.py # Interface with the USB camera
│   │   └── vision_processing.py # Process images for ball, field, obstacles, etc.
│   │
│   ├── scoring/           # Logic for scoring in goals A or B
│   │   ├── __init__.py
│   │   └── score.py        # Determine how to score detected balls
│   │
│   └── game_logic/        # Game logic for competition
│       ├── __init__.py
│       ├── game_rules.py  # Rules of the competition
│       └── competition.py # Manage competition flow and scoring
│
├── tests/                 # Unit tests for the project components
│   ├── test_motor_control.py
│   ├── test_camera_control.py
│   ├── test_vision_processing.py
│   ├── test_score.py
│   └── test_competition.py
│
├── data/                  # Data files, like images for testing detection
│
├── docs/                  # Documentation files
│   └── architecture.md    # Description of project architecture
│
└── scripts/               # Utility scripts, e.g., setup or install scripts
    ├── setup_env.sh       # Script to set up development environment
    └── run_tests.sh       # Script to run all unit tests
