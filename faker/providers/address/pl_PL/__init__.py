# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as AddressProvider


class Provider(AddressProvider):
    cities = (
        'Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk',
        'Szczecin',
        'Bydgoszcz', 'Lublin', 'Katowice', 'Białystok', 'Gdynia',
        'Częstochowa', 'Radom', 'Sosnowiec', 'Toruń', 'Kielce', 'Gliwice',
        'Rzeszów', 'Zabrze', 'Bytom', 'Olsztyn', 'Bielsko-Biała',
        'Ruda Śląska',
        'Rybnik', 'Tychy', 'Dąbrowa Górnicza', 'Gorzów Wielkopolski',
        'Elbląg',
        'Płock', 'Opole', 'Wałbrzych', 'Zielona Góra', 'Włocławek', 'Tarnów',
        'Chorzów', 'Koszalin', 'Kalisz', 'Legnica', 'Grudziądz', 'Słupsk',
        'Jaworzno', 'Jastrzębie-Zdrój', 'Nowy Sącz', 'Jelenia Góra', 'Konin',
        'Piotrków Trybunalski', 'Siedlce', 'Inowrocław', 'Mysłowice', 'Piła',
        'Lubin', 'Ostrów Wielkopolski', 'Ostrowiec Świętokrzyski', 'Gniezno',
        'Stargard Szczeciński', 'Siemianowice Śląskie', 'Suwałki', 'Głogów',
        'Pabianice', 'Chełm', 'Zamość', 'Tomaszów Mazowiecki', 'Leszno',
        'Przemyśl', 'Stalowa Wola', 'Kędzierzyn-Koźle', 'Łomża', 'Żory',
        'Mielec', 'Tarnowskie Góry', 'Tczew', 'Bełchatów', 'Świdnica',
        'Ełk', 'Pruszków', 'Będzin', 'Biała Podlaska', 'Zgierz',
        'Piekary Śląskie', 'Racibórz', 'Legionowo', 'Ostrołęka',
        'Świętochłowice', 'Starachowice', 'Zawiercie', 'Wejherowo',
        'Puławy', 'Wodzisław Śląski', 'Starogard Gdański', 'Skierniewice',
        'Tarnobrzeg', 'Skarżysko-Kamienna', 'Radomsko', 'Krosno', 'Rumia',
        'Dębica', 'Kołobrzeg', 'Kutno', 'Nysa', 'Ciechanów', 'Otwock',
        'Piaseczno', 'Zduńska Wola', 'Sieradz', 'Świnoujście', 'Żyrardów',
        'Szczecinek', 'Świdnik', 'Chojnice', 'Nowa Sól', 'Oświęcim',
        'Bolesławiec', 'Mińsk Mazowiecki', 'Mikołów', 'Jarosław', 'Sanok',
        'Knurów', 'Malbork', 'Żary', 'Kwidzyn', 'Chrzanów', 'Sopot',
        'Sochaczew', 'Wołomin', 'Oleśnica', 'Brzeg', 'Olkusz', 'Jasło',
        'Cieszyn', 'Kraśnik', 'Lębork', 'Czechowice-Dziedzice', 'Dzierżoniów',
        'Ostróda', 'Police', 'Nowy Targ', 'Iława', 'Czeladź', 'Myszków',
        'Żywiec', 'Zgorzelec', 'Oława', 'Bielawa', 'Swarzędz', 'Mława',
        'Ząbki', 'Łuków', 'Augustów', 'Śrem', 'Bochnia', 'Luboń', 'Giżycko',
        'Grodzisk Mazowiecki', 'Łowicz', 'Krotoszyn', 'Września',
        'Turek', 'Pruszcz Gdański', 'Brodnica', 'Gorlice',
        'Czerwionka-Leszczyny', 'Kłodzko', 'Marki', 'Nowy Dwór Mazowiecki',
        'Kętrzyn', 'Zakopane', 'Wyszków', 'Biłgoraj', 'Żagań',
        'Bielsk Podlaski', 'Świecie', 'Wałcz', 'Jarocin', 'Pszczyna',
        'Wągrowiec', 'Szczytno', 'Białogard', 'Sandomierz', 'Bartoszyce',
        'Kluczbork', 'Lubliniec', 'Skawina', 'Jawor', 'Kościan', 'Wieluń',
        'Kościerzyna', 'Nowa Ruda', 'Świebodzice', 'Koło', 'Piastów',
        'Goleniów', 'Ostrów Mazowiecka', 'Polkowice', 'Lubartów', 'Zambrów',
        'Płońsk', 'Reda', 'Łaziska Górne', 'Środa Wielkopolska'
    )

    street_prefixes = (
        'ulica', 'aleja', 'plac',
    )

    streets = (
        'Polna', 'Leśna', 'Słoneczna', 'Krótka', 'Szkolna', 'Ogrodowa',
        'Lipowa', 'Brzozowa', 'Ląkowa', 'Kwiatowa', 'Sosnowa', 'Kościelna',
        'Akacjowa', 'Parkowa', 'Zielona', 'Kolejowa', 'Sportowa', 'Dębowa',
        'Kościuszki', 'Maja', 'Mickiewicza', 'Cicha', 'Spokojna', 'Klonowa',
        'Spacerowa', 'Świerkowa', 'Kasztanowa', 'Nowa', 'Piaskowa',
        'Sienkiewicza', 'Różana', 'Topolowa', 'Wiśniowa', 'Dworcowa',
        'Wiejska', 'Graniczna', 'Słowackiego', 'Długa', 'Wrzosowa',
        'Konopnickiej', 'Boczna', 'Wąska', 'Wierzbowa', 'Jaśminowa',
        'Wspólna', 'Modrzewiowa', 'Kopernika', 'Jana Pawła II',
        'Poprzeczna', 'Wesoła', 'Pogodna', 'Żeromskiego', 'Rynek', 'Bukowa',
        'Wojska Polskiego', 'Sadowa', 'Górna', 'Jodłowa', 'Wolności',
        'Glówna', 'Młyśska', 'Strażacka', 'Prusa', 'Jesionowa', 'Przemysłowa',
        'Osiedlowa', 'Wiosenna', 'Sikorskiego', 'Chopina', 'Południowa',
        'Malinowa', 'Stawowa', 'Reymonta', 'Piłsudskiego', 'Zacisze',
        'Cmentarna', 'Okrężna', 'Kochanowskiego', 'Armii Krajowej', 'Miła',
        'Jasna', 'Wodna', 'Zamkowa', 'Witosa', 'Reja', 'Warszawska',
        'Miodowa', 'Partyzantów', 'Krzywa', 'Kilinskiego', 'Dolna',
        'Podgórna', 'Kreta', 'Jarzębinowa', 'Moniuszki', 'Targowa', 'Prosta',
        'Orzeszkowej', 'Spóldzielcza', 'Jagodowa', 'Działkowa', 'Staszica',
        'Orzechowa', 'Rzemieślnicza', 'Rzeczna', 'Boleslawa Chrobrego',
        'Fabryczna', 'Tęczowa', 'Chabrowa', 'Poziomkowa', 'Konwaliowa',
        'Wyszyńskiego', 'Kalinowa', 'Pólnocna', 'Matejki', 'Grunwaldzka',
        'Cisowa', 'Nadrzeczna', 'Pocztowa', 'Zachodnia', 'Dąbrowskiego',
        'Grabowa', 'Norwida', 'Źródlana', 'Asnyka', 'Gajowa', 'Paderewskiego',
        'Listopada', 'Wyspiańskiego', 'Mostowa', 'Broniewskiego', 'Tuwima',
        'Wschodnia', 'Jaworowa', 'Pozńanska', 'Makowa', 'Bema', 'Jeziorna',
        'Piękna', 'Czereśniowa', 'Mała', 'Krakowska', 'Radosna',
        'Leszczynowa', 'Traugutta', 'Jadwigi', 'Rolna', 'Wyzwolenia',
        'Piastowska', 'Grzybowa', 'Krasickiego', 'Podleśna', 'Żytnia',
        'Złota', 'Bursztynowa', 'Żwirowa', 'Stycznia', 'Widokowa',
        'Kazimierza Wielkiego', 'Kamienna', 'Jałowcowa', 'Morelowa',
        'Mieszka I', 'Myśliwska', 'Łączna', 'Szpitalna', 'Wczasowa',
        'Żurawia', 'Fiołkowa', 'Głowackiego', 'Rolnicza', 'Tulipanowa',
        'Wladysława Jagielly', 'Dworska', 'Letnia', 'Liliowa', 'Owocowa',
        'Pułaskiego', 'Stefana Batorego', 'Harcerska', 'Kołłątaja',
        'Strzelecka', 'Kraszewskiego', 'Władyslawa Łokietka',
        'Żwirki i Wigury', 'Wrocławska', 'Gdańska', 'Turystyczna',
        'Niepodleglości', 'Poniatowskiego', 'Korczaka', 'Rybacka',
        'Narutowicza', 'Okrzei', 'Krucza', 'Jagiellośska', 'Świerczewskiego',
        'Kasprowicza', 'Szeroka', 'Jana III Sobieskiego', 'Młynarska',
        'Olchowa', 'Powstańców Śląskich', 'Rumiankowa', 'Stroma',
        'Starowiejska', 'Mazowiecka',
        'Lawendowa', 'Robotnicza', 'Zbożowa', 'Mokra',
        'Powstańców Wielkopolskich', 'Towarowa', 'Dobra', 'Środkowa',
        'Willowa', 'Zielna', 'Zdrojowa', 'Opolska', 'Agrestowa', 'Księżycowa',
        'Zwycięstwa', 'Fredry', 'Letniskowa', 'Andersa', 'Baczyńskiego',
        'Batalionów Chłopskich', 'Dąbrowskiej', 'Orła', 'Skłodowskiej-Curie',
        'Blękitna', 'Rubinowa', 'Brzoskwiniowa', 'Urocza', 'Gałczyńskiego',
        'Krasińskiego', 'Pomorska', 'Szymanowskiego', 'Jeżynowa',
        'Czarnieckiego', 'Nałkowskiej', 'Zaciszna', 'Porzeczkowa',
        'Krańcowa', 'Jesienna', 'Klasztorna', 'Irysowa', 'Niecała',
        'Wybickiego', 'Nadbrzeżna', 'Szarych Szeregów', 'Wałowa',
        'Słowicza', 'Strumykowa', 'Drzymały', 'Gołębia', 'Torowa',
        'Cegielniana', 'Cyprysowa', 'Słowiańska', 'Diamentowa', 'Waryńskiego',
        'Częstochowska', 'Dojazdowa', 'Przechodnia', 'Hallera', 'Lubelska',
        'Plater', 'Popiełuszki', 'Borówkowa', 'Chełmonskiego', 'Daszyńskiego',
        'Plażowa', 'Tartaczna', 'Jabłoniowa', 'Kossaka', 'Skargi', 'Ludowa',
        'Sokoła', 'Azaliowa', 'Szmaragdowa', 'Lipca', 'Staffa', 'Tysiąclecia',
        'Brzechwy', 'Jastrzębia', 'Kusocińskiego', 'Storczykowa', 'Wilcza',
        'Górnicza', 'Szafirowa', 'Długosza', 'Handlowa', 'Krokusowa',
        'Składowa', 'Widok', 'Perłowa', 'Skośna', 'Wypoczynkowa', 'Chmielna',
        'Jaskółcza', 'Nowowiejska', 'Piwna', 'Śląska', 'Zaułek', 'Głogowa',
        'Górska', 'Truskawkowa', 'Kaszubska', 'Kosynierów', 'Mazurska',
        'Srebrna', 'Bociania', 'Ptasia', 'Cedrowa', 'Rycerska',
        'Wieniawskiego', 'Żabia', 'Toruńska', 'Podmiejska', 'Słonecznikowa',
        'Sowia', 'Stolarska', 'Powstańców', 'Sucharskiego',
        'Bolesława Krzywoustego', 'Konarskiego',
        'Szczęśliwa', 'Lazurowa', 'Miarki', 'Narcyzowa', 'Browarna',
        'Konstytucji 3 Maja', 'Majowa', 'Miłosza', 'Malczewskiego', 'Orkana',
        'Skrajna', 'Bankowa', 'Bydgoska', 'Piekarska', 'Żeglarska', 'Jana',
        'Turkusowa', 'Tylna', 'Wysoka', 'Zakątek', 'Maczka', 'Morska',
        'Rataja', 'Szewska', 'Podwale', 'Pałacowa', 'Magnoliowa', 'Ceglana',
        'Sawickiej', 'Ściegiennego', 'Wiklinowa', 'Zakole', 'Borowa',
        'Kolorowa', 'Lisia', 'Lotnicza', 'Sarnia', 'Wiązowa', 'Grottgera',
        'Kolonia', 'Królewska', 'Promienna', 'Daleka', 'Jana Sobieskiego',
        'Rejtana', 'Wiatraczna', 'Kaliska', 'Lanowa', 'Średnia', 'Wiślana',
        'Wróblewskiego', 'Koralowa', 'Kruczkowskiego', 'Lelewela',
        'Makuszyńskiego', 'Sybiraków', 'Kowalska', 'Morcinka', 'Odrzańska',
        'Okulickiego', 'Solidarności', 'Zapolskiej', 'Łabędzia', 'Wojciecha',
        'Bałtycka', 'Lwowska', 'Rajska', 'Korfantego', 'Pszenna', 'Ciasna',
        'Floriana', 'Hutnicza', 'Kielecka'
    )

    regions = (
        "Dolnośląskie", "Kujawsko-Pomorskie", "Lubelskie", "Lubuskie",
        "Łódzkie", "Małopolskie", "Mazowieckie", "Opolskie", "Podkarpackie",
        "Podlaskie", "Pomorskie", "Śląskie", "Świętokrzyskie",
        "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie",
    )

    building_number_formats = ('##', '###', "##/##",)
    postcode_formats = ('##-###',)
    street_address_formats = (
        '{{street_prefix}} {{street_name}} {{building_number}}',
        '{{street_prefix_short}} {{street_name}} {{building_number}}',
    )
    address_formats = (
        "{{street_address}}\n{{postcode}} {{city}}",
    )

    @classmethod
    def street_prefix(cls):
        """
        Randomly returns a street prefix
        :example 'aleja'
        """
        return cls.random_element(cls.street_prefixes)

    @classmethod
    def street_prefix_short(cls):
        """
        Randomly returns an abbreviation of the street prefix.
        :example 'al.'
        """
        return cls.random_element(cls.street_prefixes)[:2]+'.'

    @classmethod
    def street_name(cls):
        """
        Randomly returns a street name
        :example 'Wróblewskiego'
        """
        return cls.random_element(cls.streets)

    @classmethod
    def city(cls):
        """
        Randomly returns a street name
        :example 'Konin'
        """
        return cls.random_element(cls.cities)

    @classmethod
    def region(cls):
        """
        :example 'Wielkopolskie'
        """
        return cls.random_element(cls.regions)
