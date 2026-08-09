#!/usr/bin/env python3
"""
Squad-season pool with MY OWN estimated ratings. No scraped or third-party data.

Every card is a player in a specific season for a specific club, so a spin returns a real
roster - "Manchester United 2007-08" deals Ronaldo, Rooney, Scholes, Vidic and company at
that season's level. Every squad is from the last twenty years. Peak seasons carry peak numbers, which is why there is no separate
"icon" tier: prime Ronaldo simply is the 2007-08 card.

Ten categories: Finishing, Passing, Defending, Creativity, Soccer IQ, Dribbling,
Physical, Height, Weak Foot, Skill Moves.

Seven are hand-set on a position-normalised scale - a centre-back's Finishing of 24 and a
striker's Defending of 24 both mean "poor for that role". Three are derived from a real
fact so they stay internally consistent:
  Height       cm mapped linearly over 165-195 -> 20-99
  Weak Foot    1-5 stars -> 20/40/58/78/95
  Skill Moves  1-5 stars -> 20/40/58/78/95
The raw fact travels with the card so the board can show "189cm" or "5 stars".
"""
import json, collections, os

ATTRS = ["finishing","passing","defending","creativity","iq","dribbling","physical",
         "height","weakfoot","skillmoves"]
GRP = {"ST":"FWD","LW":"FWD","RW":"FWD","AM":"MID","CM":"MID","DM":"MID",
       "LB":"DEF","RB":"DEF","WB":"DEF","CB":"DEF"}
POSNAME = {"ST":"Striker","LW":"Left Wing","RW":"Right Wing","AM":"Attacking Mid",
           "CM":"Centre Mid","DM":"Defensive Mid","LB":"Left Back","RB":"Right Back",
           "WB":"Wing Back","CB":"Centre Back"}
STAR = {1:20, 2:40, 3:58, 4:78, 5:95}
h = lambda cm: max(20, min(99, round(20 + (cm - 165) / 30.0 * 79)))

SQUADS = []
def squad(club, season, league, rows):
    team = f"{club} {season}"
    out = []
    for (name, pos, cm, wf, sm, fin, pas, dfn, cre, iq, dri, phy) in rows:
        out.append(dict(finishing=fin, passing=pas, defending=dfn, creativity=cre, iq=iq,
                        dribbling=dri, physical=phy, height=h(cm), weakfoot=STAR[wf],
                        skillmoves=STAR[sm], name=name, team=team, club=club, season=season,
                        league=league, pos=POSNAME[pos], grp=GRP[pos], cm=cm, wf=wf, sm=sm))
    SQUADS.append(out)

#                name                 pos  cm  wf sm fin pas def cre  iq dri phy
squad("Manchester United","2007-08","Premier League",[
 ("Cristiano Ronaldo",    "RW",187, 5, 5, 96, 76, 32, 86, 86, 94, 88),
 ("Wayne Rooney",         "ST",176, 4, 4, 86, 84, 52, 84, 88, 84, 88),
 ("Carlos Tevez",         "ST",173, 3, 4, 84, 74, 44, 78, 82, 86, 82),
 ("Paul Scholes",         "CM",170, 4, 3, 82, 96, 62, 92, 96, 76, 62),
 ("Rio Ferdinand",        "CB",189, 3, 2, 26, 82, 94, 32, 94, 66, 88),
 ("Nemanja Vidic",        "CB",189, 3, 2, 34, 66, 95, 28, 88, 54, 96),
 ("Patrice Evra",         "LB",175, 3, 3, 40, 78, 86, 66, 86, 80, 84)])

squad("Manchester United","2014-15","Premier League",[
 ("Wayne Rooney",         "ST",176, 4, 4, 84, 84, 54, 82, 88, 78, 86),
 ("Angel Di Maria",       "LW",180, 3, 4, 78, 88, 40, 90, 84, 88, 66),
 ("Juan Mata",            "AM",170, 3, 4, 78, 88, 36, 90, 88, 82, 52),
 ("Ander Herrera",        "CM",182, 3, 3, 70, 84, 74, 80, 86, 78, 74),
 ("Daley Blind",          "CB",180, 4, 2, 40, 88, 78, 66, 90, 66, 62),
 ("Marcos Rojo",          "CB",187, 4, 2, 30, 72, 82, 30, 76, 58, 86),
 ("Marouane Fellaini",    "CM",194, 2, 2, 70, 66, 74, 52, 72, 58, 94)])

squad("Barcelona","2010-11","La Liga",[
 ("Lionel Messi",         "RW",170, 3, 4, 97, 92, 30, 99,100,100, 60),
 ("Xavi",                 "CM",170, 3, 3, 58,100, 66, 94,100, 88, 58),
 ("Andres Iniesta",       "CM",171, 4, 4, 66, 95, 60, 96, 97, 96, 60),
 ("David Villa",          "ST",175, 4, 4, 92, 78, 34, 82, 88, 86, 70),
 ("Sergio Busquets",      "DM",189, 3, 2, 40, 92, 86, 66, 98, 70, 78),
 ("Carles Puyol",         "CB",178, 2, 2, 28, 76, 95, 32, 92, 62, 92),
 ("Dani Alves",           "RB",172, 3, 4, 62, 88, 80, 88, 88, 88, 78)])

squad("Barcelona","2014-15","La Liga",[
 ("Lionel Messi",         "RW",170, 3, 4, 96, 92, 30, 98, 99, 99, 62),
 ("Neymar",               "LW",175, 4, 5, 90, 82, 32, 92, 86, 97, 66),
 ("Luis Suarez",          "ST",182, 4, 4, 95, 82, 38, 86, 90, 88, 84),
 ("Ivan Rakitic",         "CM",184, 4, 3, 74, 88, 72, 84, 88, 78, 76),
 ("Sergio Busquets",      "DM",189, 3, 2, 40, 92, 86, 66, 98, 70, 78),
 ("Gerard Pique",         "CB",194, 3, 2, 34, 86, 92, 40, 92, 62, 88),
 ("Jordi Alba",           "LB",170, 2, 3, 52, 82, 80, 78, 86, 84, 74)])

squad("Real Madrid","2016-17","La Liga",[
 ("Cristiano Ronaldo",    "LW",187, 5, 5, 99, 76, 30, 82, 88, 88, 92),
 ("Karim Benzema",        "ST",185, 4, 4, 88, 86, 32, 88, 92, 86, 80),
 ("Gareth Bale",          "RW",185, 4, 4, 90, 78, 46, 84, 82, 88, 92),
 ("Luka Modric",          "CM",172, 4, 4, 66, 96, 68, 94, 98, 94, 62),
 ("Toni Kroos",           "CM",183, 5, 3, 70, 99, 66, 92, 97, 76, 70),
 ("Sergio Ramos",         "CB",184, 3, 2, 46, 78, 94, 40, 90, 66, 94),
 ("Marcelo",              "LB",174, 3, 5, 60, 84, 68, 88, 84, 92, 72)])

squad("Real Madrid","2024-25","La Liga",[
 ("Kylian Mbappe",        "ST",178, 4, 5, 96, 64, 22, 76, 84, 92, 78),
 ("Jude Bellingham",      "AM",186, 4, 4, 84, 86, 72, 86, 90, 86, 86),
 ("Vinicius Junior",      "LW",176, 3, 5, 84, 68, 30, 86, 76, 96, 68),
 ("Federico Valverde",    "CM",182, 5, 3, 74, 88, 84, 76, 88, 80, 88),
 ("Antonio Rudiger",      "CB",190, 3, 2, 24, 74, 92, 26, 84, 58, 92),
 ("Eduardo Camavinga",    "DM",182, 4, 4, 46, 84, 84, 66, 84, 88, 82),
 ("Aurelien Tchouameni",  "DM",188, 3, 2, 44, 86, 88, 60, 88, 70, 88)])

squad("AC Milan","2006-07","Serie A",[
 ("Kaka",                 "AM",186, 4, 4, 88, 86, 34, 94, 90, 94, 80),
 ("Andrea Pirlo",         "DM",177, 3, 3, 74,100, 58, 96, 98, 78, 62),
 ("Clarence Seedorf",     "CM",176, 5, 4, 80, 90, 62, 88, 92, 84, 82),
 ("Gennaro Gattuso",      "DM",177, 2, 2, 40, 70, 88, 44, 80, 58, 94),
 ("Paolo Maldini",        "CB",186, 4, 2, 30, 84, 99, 40, 98, 70, 88),
 ("Alessandro Nesta",     "CB",187, 3, 2, 26, 80, 96, 32, 96, 66, 88),
 ("Filippo Inzaghi",      "ST",181, 4, 2, 92, 58, 26, 54, 90, 62, 66)])

squad("Chelsea","2009-10","Premier League",[
 ("Didier Drogba",        "ST",189, 4, 3, 94, 68, 34, 66, 84, 76,100),
 ("Frank Lampard",        "CM",184, 4, 3, 90, 88, 70, 86, 92, 74, 82),
 ("Michael Essien",       "DM",177, 4, 3, 70, 78, 90, 66, 84, 76, 96),
 ("Florent Malouda",      "LW",182, 3, 4, 80, 78, 44, 82, 80, 84, 78),
 ("John Terry",           "CB",187, 3, 2, 36, 74, 94, 30, 92, 56, 92),
 ("Ashley Cole",          "LB",176, 2, 3, 48, 78, 88, 72, 88, 80, 82),
 ("Branislav Ivanovic",   "CB",185, 3, 2, 44, 70, 88, 34, 84, 58, 92)])

squad("Arsenal","2023-24","Premier League",[
 ("Bukayo Saka",          "RW",178, 3, 4, 82, 80, 46, 90, 84, 88, 72),
 ("Martin Odegaard",      "AM",178, 3, 4, 72, 92, 42, 96, 92, 84, 58),
 ("Declan Rice",          "DM",188, 3, 2, 50, 84, 92, 60, 88, 70, 90),
 ("William Saliba",       "CB",192, 3, 2, 22, 84, 94, 28, 88, 68, 90),
 ("Gabriel Magalhaes",    "CB",190, 3, 2, 40, 78, 90, 26, 84, 56, 92),
 ("Kai Havertz",          "ST",193, 4, 3, 80, 82, 50, 80, 84, 78, 84),
 ("Gabriel Martinelli",   "LW",176, 3, 4, 74, 66, 44, 74, 74, 86, 70)])

squad("Liverpool","2018-19","Premier League",[
 ("Mohamed Salah",        "RW",175, 4, 4, 94, 76, 34, 90, 88, 90, 74),
 ("Sadio Mane",           "LW",174, 3, 4, 90, 74, 40, 84, 84, 90, 82),
 ("Roberto Firmino",      "ST",181, 4, 4, 80, 86, 56, 90, 92, 88, 80),
 ("Virgil van Dijk",      "CB",195, 3, 2, 26, 86, 97, 34, 96, 60, 94),
 ("Trent Alexander-Arnold","RB",175, 2, 3, 58, 96, 62, 96, 88, 76, 66),
 ("Andrew Robertson",     "LB",178, 2, 3, 46, 86, 82, 86, 88, 78, 80),
 ("Fabinho",              "DM",188, 3, 2, 44, 84, 90, 58, 90, 70, 88)])

squad("Bayern Munich","2012-13","Bundesliga",[
 ("Arjen Robben",         "RW",180, 2, 4, 90, 78, 36, 88, 84, 94, 72),
 ("Franck Ribery",        "LW",170, 4, 5, 84, 84, 40, 92, 86, 94, 74),
 ("Thomas Muller",        "AM",186, 3, 2, 84, 82, 50, 86, 96, 66, 74),
 ("Bastian Schweinsteiger","CM",183, 4, 3, 74, 92, 78, 86, 94, 80, 82),
 ("Philipp Lahm",         "RB",170, 4, 3, 56, 90, 88, 80, 98, 84, 74),
 ("Jerome Boateng",       "CB",192, 3, 2, 28, 84, 90, 34, 88, 62, 92),
 ("David Alaba",          "LB",180, 4, 3, 62, 86, 84, 80, 90, 84, 82)])

squad("Inter","2009-10","Serie A",[
 ("Diego Milito",         "ST",178, 3, 3, 92, 74, 32, 76, 90, 78, 78),
 ("Samuel Eto'o",         "ST",180, 3, 4, 92, 72, 40, 78, 88, 88, 86),
 ("Wesley Sneijder",      "AM",170, 4, 4, 84, 94, 48, 94, 92, 84, 62),
 ("Esteban Cambiasso",    "DM",177, 3, 2, 62, 84, 88, 70, 94, 70, 82),
 ("Javier Zanetti",       "RB",178, 4, 3, 56, 82, 88, 74, 94, 78, 88),
 ("Lucio",                "CB",188, 2, 2, 40, 70, 90, 30, 84, 58, 94),
 ("Maicon",               "RB",184, 3, 3, 66, 78, 82, 78, 82, 84, 92)])

squad("Manchester City","2022-23","Premier League",[
 ("Erling Haaland",       "ST",195, 4, 3, 99, 45, 22, 42, 78, 55, 96),
 ("Kevin De Bruyne",      "CM",181, 4, 4, 82, 99, 58, 99, 96, 82, 78),
 ("Rodri",                "DM",191, 4, 2, 48, 96, 94, 66, 97, 70, 84),
 ("Bernardo Silva",       "AM",173, 3, 5, 74, 90, 62, 92, 94, 94, 60),
 ("Ruben Dias",           "CB",187, 3, 2, 25, 80, 95, 30, 90, 52, 88),
 ("John Stones",          "CB",188, 3, 3, 34, 88, 88, 52, 92, 72, 82),
 ("Jack Grealish",        "LW",180, 2, 4, 62, 84, 44, 88, 86, 92, 78)])

squad("Paris Saint-Germain","2017-18","Ligue 1",[
 ("Neymar",               "LW",175, 4, 5, 92, 84, 32, 96, 88, 98, 68),
 ("Kylian Mbappe",        "ST",178, 4, 5, 90, 66, 24, 78, 80, 92, 76),
 ("Edinson Cavani",       "ST",184, 3, 3, 92, 66, 46, 62, 84, 70, 88),
 ("Marco Verratti",       "CM",165, 3, 4, 44, 94, 74, 88, 94, 92, 58),
 ("Angel Di Maria",       "RW",180, 3, 4, 78, 88, 40, 90, 84, 88, 66),
 ("Marquinhos",           "CB",183, 3, 2, 24, 82, 90, 30, 90, 62, 82),
 ("Thiago Silva",         "CB",183, 3, 2, 28, 84, 94, 34, 96, 68, 84)])

squad("Barcelona","2008-09","La Liga",[
 ("Lionel Messi",         "RW",170, 3, 4, 94, 88, 30, 96, 96, 98, 58),
 ("Samuel Eto'o",         "ST",180, 3, 4, 92, 72, 40, 78, 88, 88, 86),
 ("Thierry Henry",        "LW",188, 4, 4, 88, 82, 34, 86, 90, 88, 82),
 ("Xavi",                 "CM",170, 3, 3, 58, 99, 66, 94, 99, 88, 58),
 ("Andres Iniesta",       "CM",171, 4, 4, 66, 94, 60, 95, 96, 95, 60),
 ("Carles Puyol",         "CB",178, 2, 2, 28, 76, 94, 32, 92, 62, 92),
 ("Yaya Toure",           "DM",189, 3, 4, 74, 84, 84, 74, 84, 84, 96)])

squad("Borussia Dortmund","2012-13","Bundesliga",[
 ("Robert Lewandowski",   "ST",185, 4, 3, 92, 74, 30, 70, 90, 78, 86),
 ("Marco Reus",           "LW",180, 4, 4, 86, 84, 40, 90, 86, 90, 70),
 ("Mario Gotze",          "AM",176, 4, 4, 80, 86, 36, 90, 88, 90, 58),
 ("Ilkay Gundogan",       "CM",180, 4, 3, 68, 90, 74, 84, 90, 82, 68),
 ("Mats Hummels",         "CB",191, 3, 2, 30, 88, 90, 44, 94, 62, 88),
 ("Lukasz Piszczek",      "RB",184, 3, 3, 56, 78, 82, 74, 82, 76, 82),
 ("Neven Subotic",        "CB",192, 2, 2, 26, 70, 86, 24, 82, 52, 90)])

squad("Atletico Madrid","2013-14","La Liga",[
 ("Diego Costa",          "ST",188, 3, 3, 90, 66, 44, 66, 82, 76, 94),
 ("David Villa",          "ST",175, 4, 4, 88, 78, 34, 80, 88, 84, 68),
 ("Koke",                 "CM",176, 3, 3, 62, 90, 76, 88, 88, 80, 72),
 ("Gabi",                 "DM",180, 3, 2, 48, 82, 86, 66, 88, 66, 80),
 ("Diego Godin",          "CB",187, 2, 2, 44, 72, 95, 28, 94, 56, 92),
 ("Filipe Luis",          "LB",182, 3, 3, 50, 80, 84, 76, 86, 78, 80),
 ("Juanfran",             "RB",180, 3, 3, 48, 78, 82, 72, 84, 76, 80)])

squad("Juventus","2016-17","Serie A",[
 ("Gonzalo Higuain",      "ST",186, 3, 3, 92, 74, 30, 72, 88, 78, 82),
 ("Paulo Dybala",         "AM",177, 3, 4, 88, 84, 34, 90, 86, 90, 66),
 ("Miralem Pjanic",       "CM",180, 3, 4, 72, 92, 62, 90, 90, 82, 62),
 ("Leonardo Bonucci",     "CB",190, 3, 2, 30, 90, 90, 46, 94, 60, 86),
 ("Giorgio Chiellini",    "CB",187, 2, 2, 32, 72, 95, 26, 94, 54, 94),
 ("Dani Alves",           "RB",172, 3, 4, 60, 86, 78, 86, 88, 86, 74),
 ("Sami Khedira",         "CM",189, 3, 2, 66, 82, 80, 70, 86, 70, 88)])



# ---------------------------------------------------------------------------
# Full squads: the rest of each matchday group. Seven starters above plus these
# gives ~14 outfield players per season - the players who actually featured,
# rather than a 25-man list padded with academy names who never played.
# ---------------------------------------------------------------------------
def extend(club, season, league, rows):
    squad(club, season, league, rows)

#                       name                 pos  cm  wf sm fin pas def cre  iq dri phy
extend("Manchester United","2007-08","Premier League",[
 ("Ryan Giggs",           "LW",179, 2, 4, 76, 88, 46, 90, 92, 86, 66),
 ("Michael Carrick",      "CM",188, 3, 2, 52, 90, 74, 78, 92, 68, 72),
 ("Owen Hargreaves",      "CM",180, 3, 2, 56, 82, 86, 66, 88, 72, 82),
 ("Nani",                 "RW",175, 4, 5, 74, 74, 34, 80, 72, 90, 68),
 ("Ji-sung Park",         "LW",175, 3, 3, 66, 76, 72, 70, 86, 78, 84),
 ("Wes Brown",            "RB",185, 2, 2, 30, 70, 84, 40, 82, 60, 84),
 ("John O'Shea",          "CB",188, 3, 2, 34, 74, 80, 42, 82, 60, 82)])

extend("Manchester United","2014-15","Premier League",[
 ("Robin van Persie",     "ST",183, 3, 4, 88, 82, 32, 82, 88, 80, 72),
 ("Antonio Valencia",     "RB",180, 2, 3, 60, 70, 76, 66, 74, 78, 88),
 ("Ashley Young",         "LW",175, 3, 3, 62, 78, 62, 76, 78, 78, 74),
 ("Chris Smalling",       "CB",194, 2, 2, 32, 66, 84, 26, 78, 54, 90),
 ("Phil Jones",           "CB",185, 2, 2, 30, 66, 80, 26, 72, 56, 88),
 ("Luke Shaw",            "LB",185, 2, 3, 40, 74, 76, 68, 76, 78, 84),
 ("Radamel Falcao",       "ST",177, 3, 3, 78, 62, 30, 58, 80, 70, 76)])

extend("Barcelona","2010-11","La Liga",[
 ("Pedro",                "RW",169, 3, 3, 82, 78, 44, 78, 86, 82, 66),
 ("Gerard Pique",         "CB",194, 3, 2, 34, 86, 92, 40, 92, 62, 88),
 ("Eric Abidal",          "LB",186, 3, 2, 34, 74, 86, 48, 84, 70, 88),
 ("Javier Mascherano",    "DM",174, 2, 2, 30, 78, 90, 40, 90, 62, 86),
 ("Seydou Keita",         "CM",182, 3, 3, 62, 80, 78, 66, 82, 72, 84),
 ("Maxwell",              "LB",176, 2, 3, 46, 80, 76, 70, 82, 74, 74),
 ("Bojan Krkic",          "ST",170, 3, 4, 76, 76, 30, 74, 78, 82, 54)])

extend("Barcelona","2014-15","La Liga",[
 ("Xavi",                 "CM",170, 3, 3, 56, 98, 64, 92, 98, 86, 56),
 ("Dani Alves",           "RB",172, 3, 4, 60, 86, 78, 86, 88, 86, 76),
 ("Javier Mascherano",    "CB",174, 2, 2, 28, 78, 90, 38, 90, 62, 84),
 ("Pedro",                "RW",169, 3, 3, 80, 78, 44, 76, 86, 80, 66),
 ("Jeremy Mathieu",       "CB",189, 3, 2, 36, 76, 84, 34, 80, 60, 84),
 ("Rafinha",              "CM",176, 3, 4, 68, 82, 62, 78, 82, 84, 62),
 ("Adriano",              "LB",172, 4, 3, 58, 76, 72, 74, 78, 80, 74)])

extend("Real Madrid","2016-17","La Liga",[
 ("Isco",                 "AM",176, 3, 5, 76, 90, 44, 94, 90, 94, 62),
 ("Casemiro",             "DM",185, 3, 2, 52, 80, 92, 52, 88, 64, 94),
 ("Dani Carvajal",        "RB",173, 2, 3, 52, 82, 84, 80, 86, 78, 82),
 ("Raphael Varane",       "CB",191, 2, 2, 26, 78, 92, 28, 88, 60, 90),
 ("Marco Asensio",        "LW",182, 4, 4, 82, 84, 40, 86, 82, 84, 68),
 ("Alvaro Morata",        "ST",189, 3, 3, 84, 70, 34, 62, 80, 74, 84),
 ("Lucas Vazquez",        "RW",173, 3, 3, 62, 76, 58, 74, 80, 78, 74)])

extend("Real Madrid","2024-25","La Liga",[
 ("Rodrygo",              "RW",174, 4, 4, 82, 80, 40, 84, 84, 90, 66),
 ("Luka Modric",          "CM",172, 4, 4, 62, 92, 64, 90, 96, 88, 56),
 ("Eder Militao",         "CB",186, 3, 2, 28, 76, 88, 28, 84, 62, 90),
 ("Dani Carvajal",        "RB",173, 2, 3, 54, 84, 84, 82, 88, 78, 80),
 ("Ferland Mendy",        "LB",180, 2, 3, 34, 72, 82, 56, 78, 78, 84),
 ("Brahim Diaz",          "AM",171, 3, 5, 74, 80, 36, 84, 80, 92, 54),
 ("Endrick",              "ST",173, 3, 4, 80, 60, 26, 58, 72, 80, 76)])

extend("AC Milan","2006-07","Serie A",[
 ("Cafu",                 "RB",176, 3, 3, 56, 80, 84, 78, 88, 82, 88),
 ("Massimo Ambrosini",    "CM",186, 3, 2, 56, 78, 84, 60, 86, 64, 88),
 ("Marek Jankulovski",    "LB",184, 2, 3, 52, 78, 78, 72, 80, 72, 80),
 ("Kakha Kaladze",        "CB",191, 3, 2, 30, 72, 86, 32, 82, 58, 88),
 ("Alberto Gilardino",    "ST",184, 3, 3, 84, 66, 30, 60, 82, 68, 76),
 ("Serginho",             "LB",178, 2, 3, 54, 76, 72, 74, 78, 76, 78),
 ("Massimo Oddo",         "RB",180, 3, 2, 48, 76, 80, 70, 82, 68, 78)])

extend("Chelsea","2009-10","Premier League",[
 ("Nicolas Anelka",       "ST",185, 4, 4, 88, 76, 32, 76, 84, 86, 78),
 ("Michael Ballack",      "CM",189, 4, 2, 82, 84, 76, 78, 88, 68, 90),
 ("Salomon Kalou",        "LW",183, 3, 4, 76, 68, 40, 68, 72, 82, 78),
 ("Deco",                 "AM",174, 3, 4, 72, 90, 52, 90, 92, 86, 62),
 ("John Obi Mikel",       "DM",188, 3, 2, 34, 82, 84, 54, 84, 70, 86),
 ("Alex",                 "CB",192, 3, 2, 48, 66, 88, 28, 80, 52, 94),
 ("Jose Bosingwa",        "RB",180, 3, 3, 52, 74, 78, 72, 78, 78, 82)])

extend("Arsenal","2023-24","Premier League",[
 ("Gabriel Jesus",        "ST",175, 3, 4, 78, 76, 44, 78, 82, 86, 74),
 ("Leandro Trossard",     "LW",172, 4, 4, 80, 80, 40, 82, 84, 84, 62),
 ("Ben White",            "RB",186, 3, 2, 44, 82, 84, 66, 86, 70, 82),
 ("Oleksandr Zinchenko",  "LB",175, 3, 4, 46, 88, 72, 84, 88, 82, 64),
 ("Jorginho",             "DM",178, 3, 3, 46, 92, 76, 80, 92, 74, 62),
 ("Thomas Partey",        "DM",185, 3, 3, 52, 84, 86, 66, 86, 78, 88),
 ("Takehiro Tomiyasu",    "RB",188, 3, 2, 32, 76, 84, 46, 84, 66, 86)])

extend("Liverpool","2018-19","Premier League",[
 ("Jordan Henderson",     "CM",182, 3, 2, 54, 84, 80, 74, 88, 70, 86),
 ("Georginio Wijnaldum",  "CM",175, 3, 3, 66, 84, 74, 74, 86, 82, 78),
 ("James Milner",         "CM",175, 5, 3, 66, 86, 78, 78, 90, 72, 84),
 ("Joel Matip",           "CB",195, 3, 2, 30, 80, 86, 34, 84, 66, 88),
 ("Joe Gomez",            "CB",188, 2, 2, 26, 76, 84, 30, 82, 68, 88),
 ("Divock Origi",         "ST",185, 3, 3, 76, 62, 30, 58, 72, 72, 82),
 ("Xherdan Shaqiri",      "RW",169, 4, 4, 78, 82, 36, 84, 80, 84, 70)])

extend("Bayern Munich","2012-13","Bundesliga",[
 ("Mario Mandzukic",      "ST",190, 3, 2, 84, 66, 44, 60, 80, 66, 92),
 ("Toni Kroos",           "CM",183, 5, 3, 70, 94, 62, 88, 92, 74, 68),
 ("Javi Martinez",        "DM",190, 3, 2, 48, 82, 90, 56, 88, 66, 92),
 ("Dante",                "CB",187, 3, 2, 36, 76, 88, 34, 84, 62, 90),
 ("Luiz Gustavo",         "DM",187, 3, 2, 44, 78, 86, 52, 84, 64, 90),
 ("Rafinha",              "RB",172, 3, 3, 50, 78, 78, 70, 80, 76, 78),
 ("Claudio Pizarro",      "ST",186, 3, 3, 82, 74, 30, 70, 84, 72, 78)])

extend("Inter","2009-10","Serie A",[
 ("Goran Pandev",         "LW",181, 3, 3, 78, 78, 44, 78, 82, 78, 72),
 ("Thiago Motta",         "DM",187, 3, 3, 56, 86, 84, 70, 88, 72, 84),
 ("Dejan Stankovic",      "CM",182, 4, 3, 76, 84, 70, 82, 86, 76, 80),
 ("Cristian Chivu",       "CB",188, 3, 2, 34, 76, 84, 40, 82, 62, 84),
 ("Marco Materazzi",      "CB",193, 3, 2, 40, 66, 86, 26, 78, 50, 94),
 ("Mario Balotelli",      "ST",189, 3, 4, 84, 66, 28, 62, 70, 80, 90),
 ("Ivan Cordoba",         "CB",173, 2, 2, 28, 72, 86, 30, 86, 60, 82)])

extend("Manchester City","2022-23","Premier League",[
 ("Ilkay Gundogan",       "CM",180, 4, 4, 78, 90, 70, 86, 92, 84, 68),
 ("Phil Foden",           "AM",171, 4, 4, 82, 86, 42, 90, 88, 90, 55),
 ("Riyad Mahrez",         "RW",179, 2, 5, 82, 84, 34, 90, 84, 92, 58),
 ("Manuel Akanji",        "CB",188, 3, 2, 28, 84, 88, 36, 88, 68, 86),
 ("Nathan Ake",           "CB",180, 3, 2, 40, 78, 86, 34, 84, 68, 84),
 ("Kyle Walker",          "RB",183, 2, 3, 44, 74, 82, 64, 82, 76, 90),
 ("Julian Alvarez",       "ST",174, 4, 4, 84, 76, 48, 78, 86, 84, 72)])

extend("Paris Saint-Germain","2017-18","Ligue 1",[
 ("Julian Draxler",       "AM",185, 3, 4, 74, 82, 40, 84, 82, 86, 68),
 ("Adrien Rabiot",        "CM",188, 3, 3, 58, 84, 76, 74, 84, 80, 80),
 ("Presnel Kimpembe",     "CB",189, 2, 2, 26, 76, 84, 28, 80, 60, 88),
 ("Dani Alves",           "RB",172, 3, 4, 58, 84, 76, 84, 86, 84, 72),
 ("Layvin Kurzawa",       "LB",182, 2, 3, 52, 74, 74, 70, 74, 76, 80),
 ("Giovani Lo Celso",     "CM",177, 3, 4, 68, 84, 66, 82, 84, 84, 66),
 ("Thomas Meunier",       "RB",191, 3, 2, 54, 76, 78, 72, 80, 70, 86)])

extend("Barcelona","2008-09","La Liga",[
 ("Dani Alves",           "RB",172, 3, 4, 60, 86, 78, 86, 86, 86, 78),
 ("Eric Abidal",          "LB",186, 3, 2, 32, 74, 86, 46, 84, 70, 88),
 ("Rafael Marquez",       "CB",182, 3, 2, 36, 82, 86, 44, 88, 66, 82),
 ("Seydou Keita",         "CM",182, 3, 3, 64, 80, 78, 66, 82, 72, 84),
 ("Sergio Busquets",      "DM",189, 3, 2, 36, 88, 82, 60, 94, 66, 76),
 ("Bojan Krkic",          "ST",170, 3, 4, 74, 74, 30, 72, 76, 80, 54),
 ("Sylvinho",             "LB",174, 2, 3, 48, 78, 76, 72, 82, 72, 72)])

extend("Borussia Dortmund","2012-13","Bundesliga",[
 ("Jakub Blaszczykowski", "RW",176, 3, 3, 74, 80, 52, 80, 80, 82, 78),
 ("Marcel Schmelzer",     "LB",181, 2, 3, 44, 76, 80, 68, 80, 74, 80),
 ("Sven Bender",          "DM",184, 2, 2, 38, 76, 86, 48, 84, 62, 88),
 ("Sebastian Kehl",       "CM",186, 3, 2, 52, 78, 82, 60, 86, 62, 86),
 ("Kevin Grosskreutz",    "LW",184, 3, 3, 62, 74, 66, 68, 76, 72, 82),
 ("Felipe Santana",       "CB",186, 2, 2, 34, 68, 82, 26, 76, 54, 86),
 ("Ivan Perisic",         "LW",186, 4, 4, 78, 78, 46, 80, 80, 84, 82)])

extend("Atletico Madrid","2013-14","La Liga",[
 ("Arda Turan",           "LW",178, 3, 5, 76, 84, 52, 88, 84, 90, 70),
 ("Raul Garcia",          "CM",184, 3, 2, 70, 76, 76, 66, 82, 64, 88),
 ("Joao Miranda",         "CB",186, 2, 2, 30, 74, 90, 28, 90, 58, 88),
 ("Jose Sosa",            "CM",180, 3, 3, 66, 84, 62, 82, 82, 76, 70),
 ("Adrian Lopez",         "ST",176, 3, 3, 80, 70, 44, 68, 80, 78, 74),
 ("Mario Suarez",         "DM",186, 3, 2, 44, 78, 84, 56, 82, 62, 88),
 ("Toby Alderweireld",    "CB",187, 3, 2, 32, 82, 86, 38, 88, 62, 84)])

extend("Juventus","2016-17","Serie A",[
 ("Mario Mandzukic",      "LW",190, 3, 2, 80, 68, 58, 62, 82, 66, 92),
 ("Juan Cuadrado",        "RW",176, 2, 4, 70, 78, 50, 82, 78, 88, 74),
 ("Claudio Marchisio",    "CM",180, 4, 3, 70, 86, 76, 78, 88, 74, 74),
 ("Andrea Barzagli",      "CB",187, 2, 2, 24, 74, 90, 26, 92, 54, 84),
 ("Alex Sandro",          "LB",181, 3, 3, 56, 78, 80, 74, 80, 80, 86),
 ("Stephan Lichtsteiner", "RB",182, 3, 2, 52, 76, 78, 70, 82, 72, 84),
 ("Kwadwo Asamoah",       "LB",180, 3, 3, 52, 78, 74, 72, 78, 78, 80)])

POOL = [p for s in SQUADS for p in s]

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "players_own.json")
    per = collections.Counter(p["team"] for p in POOL)
    thin = [t for t, n in per.items() if n < 5]
    assert not thin, f"squads too small to fill a 5-card board: {thin}"
    ceil = {a: max(p[a] for p in POOL) for a in ATTRS}
    weak = [a for a, v in ceil.items() if v < 95]
    assert not weak, f"no elite option for {weak} - a top build would be impossible"
    json.dump({"source": "Original squad-season pool - estimated ratings, no third-party data",
               "attrs": ATTRS, "players": POOL}, open(out, "w"), indent=1)
    print(f"{len(POOL)} players across {len(per)} squad-seasons -> players_own.json")
    print("group split:", dict(collections.Counter(p["grp"] for p in POOL)))
    print("\nper-attribute ceiling:")
    for a in ATTRS:
        b = max(POOL, key=lambda p: p[a])
        print(f"   {a:<11}{ceil[a]:>4}   {b['name']} ({b['team']})")
    print("\nsquads:")
    for t, n in sorted(per.items()):
        print(f"   {t:<32}{n}")
