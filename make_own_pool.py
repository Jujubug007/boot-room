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

# ---------------------------------------------------------------------------
# Depth: rotation and bench. Twenty outfield players per season now, which
# covers the starting XI plus everyone who actually rotated into it.
# ---------------------------------------------------------------------------
#                       name                 pos  cm  wf sm fin pas def cre  iq dri phy
extend("Manchester United","2007-08","Premier League",[
 ("Anderson",            "CM",177, 3, 3, 60, 80, 70, 74, 78, 82, 82),
 ("Darren Fletcher",     "CM",183, 3, 2, 54, 78, 80, 60, 84, 66, 82),
 ("Gerard Pique",        "CB",194, 3, 2, 30, 80, 82, 34, 84, 58, 84),
 ("Louis Saha",          "ST",187, 3, 3, 82, 68, 30, 62, 76, 76, 84),
 ("Mikael Silvestre",    "CB",185, 4, 2, 30, 70, 78, 34, 76, 58, 84),
 ("Chris Eagles",        "RW",178, 3, 3, 62, 72, 44, 68, 70, 76, 66)])

extend("Manchester United","2014-15","Premier League",[
 ("Adnan Januzaj",       "LW",186, 3, 4, 66, 74, 38, 76, 72, 82, 66),
 ("Rafael da Silva",     "RB",172, 2, 3, 46, 70, 76, 62, 74, 76, 80),
 ("Jonny Evans",         "CB",188, 3, 2, 28, 74, 82, 32, 82, 58, 82),
 ("Tyler Blackett",      "CB",188, 2, 2, 24, 66, 70, 26, 68, 54, 78),
 ("Paddy McNair",        "CB",188, 3, 2, 30, 72, 72, 36, 72, 60, 76),
 ("James Wilson",        "ST",180, 3, 3, 70, 60, 28, 56, 66, 72, 74)])

extend("Barcelona","2010-11","La Liga",[
 ("Thiago Alcantara",    "CM",174, 4, 4, 62, 88, 62, 82, 88, 90, 62),
 ("Adriano",             "LB",172, 4, 3, 60, 78, 72, 76, 78, 82, 74),
 ("Ibrahim Afellay",     "AM",180, 3, 4, 68, 80, 44, 78, 78, 82, 66),
 ("Gabriel Milito",      "CB",178, 3, 2, 28, 78, 82, 36, 84, 62, 76),
 ("Andreu Fontas",       "CB",188, 3, 2, 24, 76, 76, 30, 76, 58, 78),
 ("Jeffren Suarez",      "RW",178, 3, 4, 66, 68, 40, 66, 70, 80, 68)])

extend("Barcelona","2014-15","La Liga",[
 ("Sergi Roberto",       "CM",178, 3, 3, 60, 84, 68, 76, 84, 80, 70),
 ("Marc Bartra",         "CB",184, 3, 2, 30, 82, 80, 38, 82, 66, 78),
 ("Thomas Vermaelen",    "CB",183, 3, 2, 34, 78, 82, 34, 82, 62, 82),
 ("Munir El Haddadi",    "ST",176, 3, 4, 72, 68, 30, 66, 72, 80, 66),
 ("Martin Montoya",      "RB",176, 2, 3, 44, 76, 76, 66, 78, 74, 74),
 ("Douglas Pereira",     "RB",180, 2, 3, 42, 70, 70, 62, 70, 70, 76)])

extend("Real Madrid","2016-17","La Liga",[
 ("James Rodriguez",     "AM",180, 3, 4, 82, 88, 40, 92, 86, 84, 66),
 ("Mateo Kovacic",       "CM",177, 4, 5, 62, 86, 68, 82, 86, 92, 74),
 ("Nacho Fernandez",     "CB",180, 3, 2, 34, 78, 84, 40, 84, 68, 80),
 ("Danilo",              "RB",184, 3, 3, 52, 76, 76, 68, 76, 76, 80),
 ("Fabio Coentrao",      "LB",179, 2, 3, 48, 76, 78, 70, 78, 76, 78),
 ("Mariano Diaz",        "ST",180, 3, 3, 78, 62, 28, 56, 70, 74, 78)])

extend("Real Madrid","2024-25","La Liga",[
 ("Arda Guler",          "AM",176, 3, 4, 76, 86, 34, 88, 84, 84, 54),
 ("Dani Ceballos",       "CM",179, 3, 4, 58, 86, 66, 82, 86, 84, 62),
 ("David Alaba",         "CB",180, 4, 3, 56, 86, 84, 76, 90, 80, 80),
 ("Fran Garcia",         "LB",169, 2, 3, 40, 74, 76, 62, 74, 78, 72),
 ("Raul Asencio",        "CB",184, 3, 2, 24, 72, 80, 26, 76, 58, 84),
 ("Lucas Vazquez",       "RB",173, 3, 3, 58, 78, 70, 74, 80, 76, 72)])

extend("AC Milan","2006-07","Serie A",[
 ("Yoann Gourcuff",      "AM",185, 3, 4, 70, 84, 40, 82, 80, 82, 66),
 ("Cristian Brocchi",    "DM",180, 3, 2, 40, 74, 80, 52, 78, 60, 82),
 ("Daniele Bonera",      "CB",184, 3, 2, 26, 72, 80, 30, 78, 58, 80),
 ("Giuseppe Favalli",    "CB",184, 3, 2, 28, 74, 82, 34, 84, 58, 78),
 ("Dario Simic",         "CB",183, 3, 2, 24, 70, 78, 28, 78, 56, 78),
 ("Alessandro Costacurta","CB",184, 2, 2, 26, 76, 86, 30, 92, 58, 74)])

extend("Chelsea","2009-10","Premier League",[
 ("Daniel Sturridge",    "ST",188, 3, 4, 80, 66, 28, 66, 74, 84, 78),
 ("Joe Cole",            "AM",173, 4, 5, 74, 82, 46, 86, 82, 88, 66),
 ("Ricardo Carvalho",    "CB",183, 2, 2, 24, 76, 92, 28, 92, 62, 84),
 ("Yuri Zhirkov",        "LW",180, 3, 4, 62, 76, 60, 76, 76, 82, 74),
 ("Paulo Ferreira",      "RB",180, 2, 2, 38, 74, 78, 60, 80, 66, 76),
 ("Juliano Belletti",    "RB",176, 3, 3, 56, 76, 76, 70, 78, 72, 80)])

extend("Arsenal","2023-24","Premier League",[
 ("Eddie Nketiah",       "ST",180, 3, 3, 74, 62, 32, 58, 70, 74, 74),
 ("Fabio Vieira",        "AM",170, 3, 4, 66, 84, 40, 84, 80, 82, 50),
 ("Emile Smith Rowe",    "AM",182, 3, 4, 70, 78, 40, 78, 78, 82, 64),
 ("Jakub Kiwior",        "CB",189, 4, 2, 26, 78, 80, 30, 78, 62, 82),
 ("Mohamed Elneny",      "DM",180, 3, 3, 40, 82, 76, 62, 82, 70, 72),
 ("Reiss Nelson",        "RW",175, 3, 4, 70, 70, 36, 72, 72, 84, 64)])

extend("Liverpool","2018-19","Premier League",[
 ("Naby Keita",          "CM",172, 3, 4, 62, 82, 74, 78, 82, 88, 72),
 ("Dejan Lovren",        "CB",188, 3, 2, 30, 74, 82, 30, 78, 58, 86),
 ("Adam Lallana",        "AM",172, 3, 4, 64, 84, 60, 82, 84, 84, 60),
 ("Daniel Sturridge",    "ST",188, 3, 4, 80, 66, 28, 66, 74, 82, 76),
 ("Alberto Moreno",      "LB",171, 2, 3, 46, 74, 70, 68, 70, 78, 72),
 ("Nathaniel Clyne",     "RB",175, 2, 3, 42, 74, 78, 64, 78, 74, 78)])

extend("Bayern Munich","2012-13","Bundesliga",[
 ("Xherdan Shaqiri",     "RW",169, 4, 4, 78, 82, 36, 84, 80, 86, 70),
 ("Holger Badstuber",    "CB",190, 3, 2, 26, 80, 84, 32, 84, 58, 84),
 ("Daniel van Buyten",   "CB",197, 2, 2, 34, 68, 82, 26, 80, 50, 92),
 ("Anatoliy Tymoshchuk", "DM",187, 3, 2, 40, 76, 82, 50, 82, 60, 84),
 ("Diego Contento",      "LB",178, 2, 3, 40, 72, 74, 62, 72, 72, 74),
 ("Emre Can",            "CM",184, 3, 3, 58, 78, 80, 62, 80, 74, 86)])

extend("Inter","2009-10","Serie A",[
 ("Walter Samuel",       "CB",183, 2, 2, 30, 70, 90, 26, 88, 54, 92),
 ("Sulley Muntari",      "CM",180, 4, 3, 68, 76, 74, 66, 76, 70, 86),
 ("Ricardo Quaresma",    "RW",175, 2, 5, 70, 76, 34, 82, 74, 90, 66),
 ("Davide Santon",       "LB",187, 3, 3, 44, 74, 74, 66, 74, 76, 78),
 ("Mancini",             "RW",178, 3, 5, 68, 74, 36, 76, 74, 86, 66),
 ("Nelson Rivas",        "CB",184, 2, 2, 24, 66, 78, 24, 74, 54, 82)])

extend("Manchester City","2022-23","Premier League",[
 ("Aymeric Laporte",     "CB",189, 5, 2, 32, 86, 86, 40, 86, 68, 84),
 ("Joao Cancelo",        "RB",182, 4, 4, 58, 88, 74, 88, 84, 88, 74),
 ("Cole Palmer",         "AM",189, 3, 4, 80, 80, 38, 86, 84, 84, 66),
 ("Rico Lewis",          "RB",169, 3, 3, 44, 82, 74, 76, 84, 80, 62),
 ("Sergio Gomez",        "LB",172, 2, 3, 48, 76, 68, 72, 74, 76, 66),
 ("Kalvin Phillips",     "DM",178, 3, 2, 40, 80, 80, 60, 80, 64, 80)])

extend("Paris Saint-Germain","2017-18","Ligue 1",[
 ("Thiago Motta",        "DM",187, 3, 3, 54, 86, 82, 70, 88, 70, 82),
 ("Javier Pastore",      "AM",187, 3, 5, 70, 86, 36, 88, 84, 90, 62),
 ("Christopher Nkunku",  "AM",175, 3, 4, 70, 80, 50, 80, 80, 84, 70),
 ("Yuri Berchiche",      "LB",180, 2, 3, 46, 76, 74, 70, 76, 74, 78),
 ("Lassana Diarra",      "DM",173, 3, 3, 40, 80, 84, 56, 84, 72, 80),
 ("Stanley Nsoki",       "CB",186, 3, 2, 24, 72, 76, 26, 74, 62, 82)])

extend("Barcelona","2008-09","La Liga",[
 ("Gerard Pique",        "CB",194, 3, 2, 32, 84, 88, 38, 88, 60, 86),
 ("Eidur Gudjohnsen",    "ST",185, 4, 4, 80, 82, 34, 80, 86, 80, 74),
 ("Alexander Hleb",      "AM",180, 3, 4, 62, 82, 44, 82, 80, 86, 62),
 ("Martin Caceres",      "CB",180, 2, 2, 26, 70, 80, 28, 76, 62, 84),
 ("Pedro",               "RW",169, 3, 3, 76, 76, 42, 74, 82, 80, 64),
 ("Victor Sanchez",      "CM",180, 3, 3, 54, 78, 70, 68, 76, 72, 70)])

extend("Borussia Dortmund","2012-13","Bundesliga",[
 ("Nuri Sahin",          "CM",181, 3, 3, 62, 86, 68, 80, 86, 76, 68),
 ("Julian Schieber",     "ST",186, 3, 3, 72, 62, 30, 56, 68, 68, 78),
 ("Moritz Leitner",      "CM",178, 3, 4, 60, 82, 62, 78, 80, 80, 62),
 ("Oliver Kirch",        "RB",184, 3, 2, 44, 74, 76, 60, 76, 66, 78),
 ("Leonardo Bittencourt","AM",172, 3, 4, 64, 78, 44, 78, 76, 84, 58),
 ("Koray Gunter",        "CB",186, 2, 2, 24, 70, 76, 26, 72, 56, 82)])

extend("Atletico Madrid","2013-14","La Liga",[
 ("Diego Ribas",         "AM",178, 3, 4, 72, 86, 52, 88, 84, 84, 66),
 ("Cristian Rodriguez",  "LW",176, 3, 3, 68, 78, 60, 78, 78, 80, 78),
 ("Emiliano Insua",      "LB",178, 2, 3, 44, 76, 76, 68, 76, 74, 78),
 ("Leo Baptistao",       "ST",180, 3, 4, 70, 68, 34, 66, 70, 80, 74),
 ("Javier Manquillo",    "RB",178, 2, 3, 40, 72, 76, 62, 74, 74, 76),
 ("Josuha Guilavogui",   "DM",188, 3, 2, 38, 74, 82, 50, 78, 62, 88)])

extend("Juventus","2016-17","Serie A",[
 ("Medhi Benatia",       "CB",190, 3, 2, 32, 76, 88, 30, 86, 60, 88),
 ("Daniele Rugani",      "CB",190, 3, 2, 26, 80, 84, 30, 84, 60, 82),
 ("Tomas Rincon",        "DM",178, 3, 2, 42, 76, 82, 52, 80, 64, 86),
 ("Mario Lemina",        "CM",184, 3, 3, 56, 78, 76, 64, 78, 74, 86),
 ("Marko Pjaca",         "LW",186, 3, 4, 70, 74, 38, 76, 74, 84, 74),
 ("Hernanes",            "CM",182, 4, 3, 70, 84, 66, 80, 82, 76, 74)])

# ---------------------------------------------------------------------------
# More ever-presents: clubs continuously in a top-five league since 2010.
# ---------------------------------------------------------------------------
squad("Tottenham Hotspur","2016-17","Premier League",[
 ("Harry Kane",          "ST",188, 4, 3, 94, 80, 32, 80, 90, 66, 84),
 ("Dele Alli",           "AM",188, 3, 4, 82, 80, 52, 84, 84, 84, 76),
 ("Christian Eriksen",   "AM",182, 3, 3, 76, 92, 46, 94, 90, 80, 58),
 ("Son Heung-min",       "LW",183, 5, 4, 86, 76, 42, 80, 84, 88, 80),
 ("Toby Alderweireld",   "CB",186, 3, 2, 30, 84, 90, 40, 92, 62, 84),
 ("Jan Vertonghen",      "CB",189, 4, 2, 32, 82, 88, 42, 90, 64, 86),
 ("Kyle Walker",         "RB",183, 2, 3, 44, 74, 80, 66, 80, 76, 90),
 ("Danny Rose",          "LB",173, 2, 3, 46, 74, 78, 70, 76, 78, 84),
 ("Victor Wanyama",      "DM",188, 3, 2, 44, 76, 86, 52, 82, 62, 94),
 ("Mousa Dembele",       "CM",185, 4, 5, 52, 86, 78, 76, 88, 94, 90),
 ("Eric Dier",           "CB",188, 3, 2, 38, 78, 82, 46, 82, 60, 84),
 ("Erik Lamela",         "RW",183, 3, 4, 70, 80, 48, 82, 78, 86, 70),
 ("Vincent Janssen",     "ST",185, 3, 2, 66, 62, 30, 54, 68, 62, 78),
 ("Ben Davies",          "LB",181, 2, 2, 38, 76, 78, 64, 78, 70, 76),
 ("Moussa Sissoko",      "CM",187, 3, 3, 52, 72, 74, 62, 72, 76, 92),
 ("Harry Winks",         "CM",178, 3, 3, 46, 84, 68, 74, 84, 76, 62),
 ("Kieran Trippier",     "RB",178, 2, 3, 50, 88, 76, 88, 84, 72, 74),
 ("Georges-Kevin Nkoudou","LW",175, 3, 4, 62, 66, 36, 66, 66, 82, 68),
 ("Kevin Wimmer",        "CB",188, 3, 2, 26, 74, 76, 28, 76, 56, 80),
 ("Cameron Carter-Vickers","CB",183, 2, 2, 24, 70, 74, 26, 72, 56, 82)])

squad("Napoli","2022-23","Serie A",[
 ("Victor Osimhen",      "ST",185, 3, 3, 92, 60, 30, 60, 80, 76, 94),
 ("Khvicha Kvaratskhelia","LW",183, 3, 5, 82, 78, 34, 90, 82, 94, 74),
 ("Stanislav Lobotka",   "DM",168, 4, 3, 40, 94, 78, 72, 94, 86, 58),
 ("Kim Min-jae",         "CB",190, 3, 2, 28, 78, 92, 30, 86, 66, 94),
 ("Piotr Zielinski",     "AM",180, 4, 4, 74, 88, 56, 86, 86, 86, 66),
 ("Andre-Frank Zambo Anguissa","CM",184, 3, 3, 58, 82, 82, 66, 82, 80, 92),
 ("Giovanni Di Lorenzo", "RB",183, 3, 3, 58, 80, 82, 74, 84, 74, 82),
 ("Mario Rui",           "LB",172, 2, 3, 42, 84, 74, 80, 82, 74, 66),
 ("Amir Rrahmani",       "CB",192, 3, 2, 34, 76, 86, 30, 82, 58, 88),
 ("Matteo Politano",     "RW",172, 3, 4, 70, 78, 50, 82, 80, 84, 60),
 ("Hirving Lozano",      "RW",175, 3, 4, 74, 70, 40, 74, 74, 86, 72),
 ("Eljif Elmas",         "AM",182, 4, 4, 70, 78, 56, 76, 78, 82, 70),
 ("Giacomo Raspadori",   "ST",172, 4, 4, 78, 78, 34, 76, 82, 82, 60),
 ("Tanguy Ndombele",     "CM",181, 3, 4, 62, 82, 66, 78, 80, 88, 82),
 ("Leo Ostigard",        "CB",186, 2, 2, 30, 68, 78, 24, 74, 54, 86),
 ("Mathias Olivera",     "LB",184, 2, 3, 40, 76, 78, 66, 78, 76, 80),
 ("Diego Demme",         "DM",176, 3, 2, 38, 80, 76, 58, 80, 68, 74),
 ("Alessio Zerbin",      "LW",182, 3, 3, 62, 68, 38, 66, 70, 76, 70),
 ("Bartosz Bereszynski", "RB",183, 3, 2, 38, 72, 76, 58, 76, 66, 78),
 ("Giovanni Simeone",    "ST",181, 3, 3, 80, 62, 34, 58, 76, 70, 82)])

squad("Sevilla","2015-16","La Liga",[
 ("Kevin Gameiro",       "ST",172, 3, 3, 84, 68, 32, 66, 80, 80, 70),
 ("Ever Banega",         "CM",175, 3, 4, 68, 90, 60, 88, 88, 86, 62),
 ("Grzegorz Krychowiak", "DM",187, 3, 2, 46, 80, 86, 56, 84, 68, 90),
 ("Vitolo",              "LW",178, 3, 4, 72, 80, 46, 82, 80, 84, 72),
 ("Adil Rami",           "CB",190, 2, 2, 34, 70, 84, 26, 80, 54, 90),
 ("Daniel Carrico",      "CB",186, 2, 2, 28, 72, 82, 26, 80, 56, 84),
 ("Coke",                "RB",180, 3, 3, 56, 76, 78, 70, 78, 72, 80),
 ("Benoit Tremoulinas",  "LB",180, 2, 3, 46, 76, 74, 70, 74, 74, 78),
 ("Michael Krohn-Dehli", "AM",176, 3, 3, 66, 80, 52, 78, 80, 78, 62),
 ("Steven NZonzi",       "DM",196, 3, 2, 46, 82, 84, 58, 84, 66, 88),
 ("Yevhen Konoplyanka",  "LW",178, 3, 4, 72, 78, 40, 80, 76, 86, 66),
 ("Fernando Llorente",   "ST",195, 3, 2, 76, 66, 34, 58, 78, 58, 88),
 ("Timothee Kolodziejczak","CB",184, 2, 2, 26, 70, 80, 26, 76, 56, 84),
 ("Sebastian Cristoforo","CM",175, 3, 3, 48, 78, 70, 66, 76, 74, 70),
 ("Mariano Ferreira",    "RB",180, 2, 3, 46, 72, 76, 64, 74, 72, 80),
 ("Ciro Immobile",       "ST",185, 3, 3, 80, 64, 30, 58, 78, 70, 78),
 ("Vicente Iborra",      "CM",190, 3, 2, 56, 78, 76, 62, 80, 62, 86),
 ("Jose Antonio Reyes",  "LW",178, 3, 4, 70, 80, 44, 80, 80, 84, 66),
 ("Nicolas Pareja",      "CB",184, 2, 2, 26, 70, 80, 24, 78, 56, 82),
 ("Cristoforo Diaz",     "CM",176, 3, 3, 46, 74, 70, 64, 74, 72, 72)])

squad("Bayer Leverkusen","2023-24","Bundesliga",[
 ("Florian Wirtz",       "AM",176, 4, 5, 78, 88, 46, 96, 92, 92, 62),
 ("Alejandro Grimaldo",  "LB",171, 2, 4, 66, 90, 66, 92, 84, 82, 62),
 ("Granit Xhaka",        "DM",186, 3, 3, 52, 94, 80, 78, 90, 70, 80),
 ("Victor Boniface",     "ST",190, 3, 3, 84, 68, 30, 66, 76, 78, 92),
 ("Jeremie Frimpong",    "WB",171, 2, 4, 68, 66, 62, 74, 72, 88, 70),
 ("Jonathan Tah",        "CB",195, 3, 2, 22, 78, 88, 26, 82, 58, 92),
 ("Edmond Tapsoba",      "CB",191, 3, 2, 26, 84, 86, 32, 84, 64, 88),
 ("Exequiel Palacios",   "CM",177, 3, 3, 60, 84, 74, 76, 82, 80, 74),
 ("Jonas Hofmann",       "RW",176, 3, 3, 72, 84, 52, 82, 84, 82, 70),
 ("Amine Adli",          "LW",175, 3, 4, 70, 74, 40, 76, 74, 86, 62),
 ("Odilon Kossounou",    "CB",191, 2, 2, 24, 74, 82, 26, 78, 62, 88),
 ("Robert Andrich",      "DM",187, 3, 2, 52, 80, 82, 60, 82, 68, 88),
 ("Nathan Tella",        "RW",175, 3, 4, 74, 70, 40, 72, 74, 84, 68),
 ("Patrik Schick",       "ST",191, 4, 3, 86, 66, 28, 62, 80, 72, 82),
 ("Piero Hincapie",      "CB",184, 3, 2, 26, 78, 84, 30, 80, 66, 84),
 ("Josip Stanisic",      "RB",184, 3, 2, 38, 76, 80, 56, 80, 68, 82),
 ("Adam Hlozek",         "ST",188, 3, 3, 74, 74, 34, 72, 76, 76, 78),
 ("Nadiem Amiri",        "AM",180, 3, 4, 66, 80, 50, 78, 78, 82, 66),
 ("Arthur",              "CM",180, 3, 3, 50, 84, 66, 72, 82, 78, 66),
 ("Borja Iglesias",      "ST",187, 3, 3, 76, 66, 30, 60, 74, 70, 80)])

squad("Olympique Lyonnais","2019-20","Ligue 1",[
 ("Memphis Depay",       "ST",176, 4, 5, 84, 84, 34, 88, 82, 90, 74),
 ("Houssem Aouar",       "AM",176, 3, 5, 72, 86, 48, 88, 84, 90, 62),
 ("Moussa Dembele",      "ST",183, 3, 3, 84, 64, 30, 62, 76, 76, 82),
 ("Karl Toko Ekambi",    "LW",185, 3, 4, 78, 68, 36, 70, 72, 82, 76),
 ("Lucas Tousart",       "DM",184, 3, 2, 48, 76, 84, 56, 80, 66, 88),
 ("Marcelo Guedes",      "CB",185, 2, 2, 30, 72, 80, 26, 76, 56, 88),
 ("Jason Denayer",       "CB",184, 3, 2, 28, 76, 82, 30, 80, 62, 84),
 ("Leo Dubois",          "RB",178, 3, 3, 48, 76, 76, 70, 76, 74, 78),
 ("Maxwel Cornet",       "LW",179, 3, 4, 72, 72, 52, 72, 74, 82, 78),
 ("Bertrand Traore",     "RW",179, 3, 4, 74, 74, 38, 76, 74, 84, 70),
 ("Thiago Mendes",       "DM",178, 3, 3, 44, 80, 80, 60, 80, 74, 80),
 ("Jeff Reine-Adelaide", "AM",185, 3, 4, 66, 80, 44, 78, 76, 86, 70),
 ("Youssouf Kone",       "LB",180, 2, 3, 40, 72, 74, 62, 72, 74, 76),
 ("Rafael da Silva",     "RB",172, 2, 3, 46, 72, 76, 64, 76, 78, 78),
 ("Fernando Marcal",     "LB",174, 2, 3, 42, 74, 76, 64, 76, 72, 76),
 ("Joachim Andersen",    "CB",192, 3, 2, 28, 80, 82, 34, 82, 60, 86),
 ("Amine Gouiri",        "ST",180, 3, 4, 72, 72, 34, 72, 74, 82, 70),
 ("Martin Terrier",      "LW",181, 3, 4, 76, 74, 40, 74, 76, 82, 70),
 ("Oumar Solet",         "CB",190, 2, 2, 24, 70, 78, 24, 74, 60, 86),
 ("Maxence Caqueret",    "CM",174, 3, 3, 48, 82, 72, 74, 82, 78, 64)])

squad("AS Roma","2013-14","Serie A",[
 ("Francesco Totti",     "AM",180, 4, 4, 88, 94, 34, 96, 96, 84, 72),
 ("Daniele De Rossi",    "DM",184, 4, 2, 66, 86, 88, 70, 90, 68, 90),
 ("Miralem Pjanic",      "CM",180, 3, 4, 72, 90, 60, 88, 88, 82, 62),
 ("Gervinho",            "LW",179, 3, 4, 74, 68, 36, 72, 70, 88, 76),
 ("Mehdi Benatia",       "CB",190, 3, 2, 32, 76, 88, 30, 86, 60, 88),
 ("Leandro Castan",      "CB",185, 2, 2, 28, 70, 84, 26, 80, 56, 86),
 ("Maicon",              "RB",184, 3, 3, 60, 76, 78, 74, 80, 80, 88),
 ("Kevin Strootman",     "CM",186, 3, 3, 62, 84, 82, 74, 84, 74, 86),
 ("Alessandro Florenzi", "RB",173, 3, 3, 64, 80, 74, 78, 80, 78, 76),
 ("Radja Nainggolan",    "CM",176, 3, 3, 74, 82, 80, 78, 84, 80, 88),
 ("Adem Ljajic",         "LW",180, 3, 4, 72, 80, 40, 82, 78, 84, 64),
 ("Vasilis Torosidis",   "RB",182, 3, 2, 46, 74, 78, 62, 78, 68, 82),
 ("Federico Balzaretti",  "LB",180, 2, 3, 44, 76, 76, 68, 78, 70, 78),
 ("Marquinho",           "RW",174, 3, 4, 62, 74, 44, 72, 72, 82, 62),
 ("Michael Bradley",     "CM",184, 3, 2, 54, 82, 76, 68, 84, 66, 80),
 ("Dodo",                "CB",183, 2, 2, 26, 70, 78, 26, 76, 58, 82),
 ("Mattia Destro",       "ST",180, 3, 3, 80, 62, 30, 58, 76, 70, 76),
 ("Rodrigo Taddei",      "RW",178, 3, 3, 58, 76, 56, 70, 76, 74, 72),
 ("Nicolas Burdisso",    "CB",180, 2, 2, 28, 70, 82, 26, 80, 54, 84),
 ("Jose Holebas",        "LB",181, 2, 3, 46, 74, 74, 68, 74, 72, 82)])

# ---------------------------------------------------------------------------
# Second seasons, so every club has a year to respin into. 14 outfield each -
# still above the eleven a board needs.
# ---------------------------------------------------------------------------
squad("AC Milan","2010-11","Serie A",[
 ("Zlatan Ibrahimovic",  "ST",195, 4, 5, 92, 80, 34, 84, 88, 84, 96),
 ("Robinho",             "LW",172, 3, 5, 78, 76, 32, 82, 76, 92, 62),
 ("Alexandre Pato",      "ST",180, 3, 4, 84, 68, 28, 68, 76, 86, 78),
 ("Clarence Seedorf",    "CM",176, 5, 4, 76, 88, 60, 86, 90, 80, 78),
 ("Thiago Silva",        "CB",183, 3, 2, 28, 84, 94, 34, 96, 68, 84),
 ("Alessandro Nesta",    "CB",187, 3, 2, 26, 78, 92, 30, 94, 62, 84),
 ("Massimo Ambrosini",   "CM",186, 3, 2, 54, 78, 82, 58, 86, 62, 86),
 ("Kevin-Prince Boateng","AM",186, 4, 4, 74, 78, 62, 78, 78, 84, 88),
 ("Ignazio Abate",       "RB",178, 2, 3, 44, 72, 76, 62, 76, 76, 84),
 ("Gennaro Gattuso",     "DM",177, 2, 2, 38, 70, 86, 42, 80, 56, 92),
 ("Mathieu Flamini",     "DM",178, 3, 2, 42, 76, 82, 52, 80, 66, 84),
 ("Antonio Cassano",     "AM",175, 3, 5, 78, 88, 30, 90, 86, 88, 60),
 ("Luca Antonini",       "LB",180, 2, 3, 40, 72, 74, 60, 72, 70, 78),
 ("Mario Yepes",         "CB",185, 2, 2, 28, 70, 84, 26, 82, 54, 86)])

squad("Chelsea","2011-12","Premier League",[
 ("Didier Drogba",       "ST",189, 4, 3, 88, 66, 34, 64, 84, 70, 96),
 ("Juan Mata",           "AM",170, 3, 4, 80, 90, 36, 92, 88, 84, 52),
 ("Frank Lampard",       "CM",184, 4, 3, 84, 86, 68, 82, 90, 70, 78),
 ("Fernando Torres",     "ST",186, 4, 4, 76, 68, 30, 68, 78, 80, 78),
 ("John Terry",          "CB",187, 3, 2, 36, 74, 90, 30, 92, 54, 88),
 ("Ashley Cole",         "LB",176, 2, 3, 46, 78, 86, 70, 88, 78, 78),
 ("Branislav Ivanovic",  "CB",185, 3, 2, 46, 72, 88, 36, 86, 58, 92),
 ("Ramires",             "CM",179, 3, 3, 66, 78, 76, 70, 78, 80, 90),
 ("David Luiz",          "CB",189, 3, 4, 44, 84, 80, 56, 76, 74, 88),
 ("Daniel Sturridge",    "ST",188, 3, 4, 80, 66, 28, 68, 74, 84, 78),
 ("Raul Meireles",       "CM",180, 3, 3, 66, 82, 68, 74, 80, 76, 78),
 ("Salomon Kalou",       "LW",183, 3, 4, 74, 68, 40, 68, 72, 82, 76),
 ("Jose Bosingwa",       "RB",180, 3, 3, 50, 74, 76, 70, 76, 78, 80),
 ("Gary Cahill",         "CB",193, 2, 2, 32, 72, 84, 28, 82, 54, 88)])

squad("Arsenal","2015-16","Premier League",[
 ("Alexis Sanchez",      "LW",169, 4, 5, 86, 80, 46, 86, 82, 92, 82),
 ("Mesut Ozil",          "AM",180, 3, 4, 70, 94, 34, 96, 92, 86, 54),
 ("Santi Cazorla",       "CM",168, 5, 4, 74, 90, 56, 88, 90, 88, 58),
 ("Olivier Giroud",      "ST",192, 3, 3, 82, 74, 34, 70, 82, 66, 88),
 ("Laurent Koscielny",   "CB",186, 2, 2, 32, 78, 90, 30, 88, 62, 84),
 ("Hector Bellerin",     "RB",178, 2, 3, 48, 76, 76, 72, 78, 82, 80),
 ("Nacho Monreal",       "LB",179, 2, 3, 42, 78, 80, 68, 82, 72, 76),
 ("Francis Coquelin",    "DM",178, 3, 2, 38, 74, 84, 50, 78, 66, 84),
 ("Aaron Ramsey",        "CM",178, 4, 3, 74, 84, 68, 82, 84, 82, 78),
 ("Theo Walcott",        "RW",176, 3, 3, 76, 68, 36, 70, 72, 84, 76),
 ("Per Mertesacker",     "CB",198, 2, 2, 30, 78, 84, 30, 90, 44, 82),
 ("Mohamed Elneny",      "DM",180, 3, 3, 40, 82, 76, 62, 82, 70, 74),
 ("Alex Oxlade-Chamberlain","RW",180, 3, 4, 70, 76, 52, 74, 74, 84, 82),
 ("Gabriel Paulista",    "CB",187, 2, 2, 28, 70, 82, 26, 78, 56, 88)])

squad("Liverpool","2024-25","Premier League",[
 ("Mohamed Salah",       "RW",175, 4, 4, 95, 78, 34, 92, 90, 88, 74),
 ("Virgil van Dijk",     "CB",195, 3, 2, 26, 86, 96, 34, 96, 60, 92),
 ("Ryan Gravenberch",    "DM",190, 3, 4, 48, 88, 82, 70, 86, 88, 84),
 ("Alexis Mac Allister", "CM",174, 3, 3, 68, 90, 76, 84, 92, 80, 70),
 ("Dominik Szoboszlai",  "AM",186, 4, 4, 76, 84, 62, 84, 84, 84, 82),
 ("Luis Diaz",           "LW",180, 3, 5, 80, 70, 40, 80, 76, 92, 76),
 ("Cody Gakpo",          "LW",189, 4, 4, 82, 72, 40, 78, 78, 82, 78),
 ("Trent Alexander-Arnold","RB",175, 2, 3, 58, 96, 62, 96, 88, 78, 66),
 ("Ibrahima Konate",     "CB",194, 3, 2, 26, 78, 88, 28, 82, 66, 92),
 ("Andrew Robertson",    "LB",178, 2, 3, 44, 84, 80, 82, 86, 76, 78),
 ("Curtis Jones",        "CM",185, 3, 4, 62, 84, 66, 78, 82, 86, 74),
 ("Diogo Jota",          "ST",178, 4, 4, 84, 70, 38, 74, 80, 84, 74),
 ("Conor Bradley",       "RB",178, 2, 3, 48, 76, 76, 72, 78, 78, 78),
 ("Wataru Endo",         "DM",178, 3, 2, 42, 76, 82, 54, 82, 66, 86)])

squad("Bayern Munich","2019-20","Bundesliga",[
 ("Robert Lewandowski",  "ST",185, 4, 3, 98, 74, 30, 72, 94, 78, 88),
 ("Thomas Muller",       "AM",186, 3, 2, 82, 86, 50, 92, 98, 64, 74),
 ("Serge Gnabry",        "RW",176, 4, 4, 84, 78, 40, 80, 80, 88, 76),
 ("Joshua Kimmich",      "CM",177, 4, 3, 58, 96, 82, 92, 96, 76, 74),
 ("Leon Goretzka",       "CM",189, 4, 3, 74, 84, 76, 78, 84, 78, 90),
 ("Alphonso Davies",     "LB",183, 3, 4, 46, 76, 78, 72, 78, 90, 82),
 ("David Alaba",         "CB",180, 4, 3, 58, 88, 86, 78, 92, 82, 82),
 ("Kingsley Coman",      "LW",180, 3, 5, 78, 74, 36, 80, 76, 92, 74),
 ("Jerome Boateng",      "CB",192, 3, 2, 28, 84, 88, 34, 88, 60, 90),
 ("Thiago Alcantara",    "CM",174, 4, 4, 64, 94, 66, 88, 94, 92, 64),
 ("Ivan Perisic",        "LW",186, 4, 4, 78, 78, 46, 80, 80, 82, 84),
 ("Benjamin Pavard",     "RB",186, 3, 2, 40, 78, 82, 56, 82, 66, 84),
 ("Niklas Sule",         "CB",195, 3, 2, 30, 76, 86, 28, 82, 56, 94),
 ("Corentin Tolisso",    "CM",181, 4, 3, 70, 82, 72, 74, 80, 78, 84)])

squad("Inter","2022-23","Serie A",[
 ("Lautaro Martinez",    "ST",174, 4, 3, 90, 68, 42, 68, 86, 80, 82),
 ("Nicolo Barella",      "CM",172, 3, 3, 68, 88, 80, 86, 90, 82, 78),
 ("Hakan Calhanoglu",    "DM",178, 3, 4, 74, 94, 74, 88, 90, 78, 72),
 ("Alessandro Bastoni",  "CB",190, 3, 2, 26, 88, 90, 56, 88, 66, 84),
 ("Federico Dimarco",    "WB",175, 2, 3, 60, 90, 70, 90, 84, 76, 68),
 ("Edin Dzeko",          "ST",193, 4, 3, 86, 78, 34, 74, 88, 68, 86),
 ("Denzel Dumfries",     "RB",188, 2, 3, 56, 70, 74, 68, 74, 76, 90),
 ("Marcelo Brozovic",    "DM",181, 3, 3, 52, 90, 76, 76, 90, 80, 74),
 ("Francesco Acerbi",    "CB",192, 2, 2, 30, 74, 88, 28, 86, 54, 88),
 ("Matteo Darmian",      "RB",183, 3, 2, 42, 78, 82, 60, 84, 70, 80),
 ("Romelu Lukaku",       "ST",191, 4, 3, 84, 64, 30, 60, 78, 66, 94),
 ("Henrikh Mkhitaryan",  "CM",177, 4, 4, 72, 86, 62, 84, 86, 84, 70),
 ("Stefan de Vrij",      "CB",189, 3, 2, 28, 80, 86, 32, 88, 58, 84),
 ("Joaquin Correa",      "ST",188, 3, 4, 72, 72, 34, 74, 74, 84, 70)])

squad("Manchester City","2017-18","Premier League",[
 ("Kevin De Bruyne",     "CM",181, 4, 4, 82, 99, 58, 99, 96, 82, 78),
 ("David Silva",         "AM",173, 3, 5, 74, 94, 44, 96, 96, 92, 54),
 ("Sergio Aguero",       "ST",173, 4, 4, 94, 74, 30, 78, 88, 88, 78),
 ("Raheem Sterling",     "RW",170, 3, 4, 84, 74, 40, 80, 78, 90, 72),
 ("Leroy Sane",          "LW",183, 3, 4, 82, 78, 36, 84, 78, 90, 74),
 ("Fernandinho",         "DM",179, 3, 3, 54, 84, 88, 66, 90, 76, 88),
 ("Nicolas Otamendi",    "CB",183, 2, 2, 34, 76, 86, 30, 80, 58, 92),
 ("Kyle Walker",         "RB",183, 2, 3, 46, 76, 80, 66, 80, 78, 92),
 ("Vincent Kompany",     "CB",190, 3, 2, 36, 78, 90, 32, 90, 58, 92),
 ("Ilkay Gundogan",      "CM",180, 4, 4, 74, 90, 68, 86, 92, 84, 66),
 ("Gabriel Jesus",       "ST",175, 3, 4, 82, 74, 40, 76, 80, 86, 74),
 ("Benjamin Mendy",      "LB",185, 2, 3, 46, 76, 74, 74, 72, 78, 86),
 ("John Stones",         "CB",188, 3, 3, 32, 86, 84, 48, 88, 70, 80),
 ("Bernardo Silva",      "AM",173, 3, 5, 72, 88, 58, 88, 92, 92, 58)])

squad("Paris Saint-Germain","2022-23","Ligue 1",[
 ("Kylian Mbappe",       "ST",178, 4, 5, 97, 66, 22, 78, 84, 94, 78),
 ("Lionel Messi",        "RW",170, 3, 4, 88, 94, 28, 96, 98, 92, 52),
 ("Neymar",              "LW",175, 4, 5, 86, 86, 30, 94, 88, 96, 64),
 ("Marco Verratti",      "CM",165, 3, 4, 46, 94, 74, 88, 94, 92, 58),
 ("Achraf Hakimi",       "RB",181, 3, 3, 62, 76, 68, 80, 78, 86, 82),
 ("Marquinhos",          "CB",183, 3, 2, 26, 84, 92, 32, 92, 64, 82),
 ("Vitinha",             "CM",172, 3, 4, 60, 90, 66, 80, 88, 88, 60),
 ("Fabian Ruiz",         "CM",189, 3, 3, 66, 88, 68, 82, 86, 82, 72),
 ("Nuno Mendes",         "LB",176, 2, 3, 44, 76, 78, 68, 76, 84, 80),
 ("Danilo Pereira",      "CB",188, 3, 2, 40, 78, 84, 50, 82, 62, 88),
 ("Sergio Ramos",        "CB",184, 3, 2, 44, 78, 88, 38, 88, 62, 90),
 ("Renato Sanches",      "CM",176, 3, 4, 60, 80, 72, 74, 78, 86, 84),
 ("Carlos Soler",        "CM",180, 3, 3, 66, 82, 62, 78, 80, 78, 72),
 ("Nordi Mukiele",       "RB",187, 3, 2, 40, 74, 80, 54, 78, 70, 86)])

squad("Borussia Dortmund","2023-24","Bundesliga",[
 ("Julian Brandt",       "AM",185, 4, 4, 72, 88, 44, 90, 86, 86, 64),
 ("Marco Reus",          "LW",180, 4, 4, 80, 84, 40, 86, 86, 84, 66),
 ("Niclas Fullkrug",     "ST",189, 3, 2, 84, 66, 32, 62, 80, 62, 90),
 ("Mats Hummels",        "CB",191, 3, 2, 30, 88, 88, 44, 96, 60, 84),
 ("Jadon Sancho",        "LW",180, 3, 5, 76, 84, 34, 88, 82, 92, 62),
 ("Karim Adeyemi",       "LW",180, 3, 4, 76, 62, 36, 70, 72, 90, 72),
 ("Ian Maatsen",         "LB",170, 2, 3, 46, 78, 74, 74, 76, 84, 72),
 ("Nico Schlotterbeck",  "CB",191, 4, 2, 26, 86, 86, 44, 84, 66, 86),
 ("Emre Can",            "DM",186, 3, 3, 56, 80, 84, 62, 82, 70, 88),
 ("Marcel Sabitzer",     "CM",177, 4, 3, 74, 84, 70, 82, 84, 80, 78),
 ("Julian Ryerson",      "RB",183, 3, 2, 42, 76, 80, 58, 80, 72, 86),
 ("Donyell Malen",       "RW",180, 3, 4, 78, 70, 34, 74, 74, 86, 74),
 ("Sebastien Haller",    "ST",190, 3, 3, 80, 70, 30, 66, 78, 70, 88),
 ("Ramy Bensebaini",     "LB",187, 2, 2, 40, 74, 80, 56, 78, 70, 86)])

squad("Atletico Madrid","2020-21","La Liga",[
 ("Luis Suarez",         "ST",182, 4, 4, 90, 78, 36, 80, 90, 80, 84),
 ("Marcos Llorente",     "CM",184, 3, 3, 76, 78, 76, 76, 82, 84, 90),
 ("Koke",                "CM",176, 3, 3, 62, 90, 78, 88, 92, 80, 72),
 ("Felipe Monteiro",     "CB",186, 2, 2, 28, 72, 86, 26, 82, 56, 90),
 ("Stefan Savic",        "CB",187, 2, 2, 28, 74, 88, 26, 84, 56, 88),
 ("Jose Maria Gimenez",  "CB",185, 3, 2, 26, 74, 90, 26, 86, 56, 90),
 ("Kieran Trippier",     "RB",178, 2, 3, 50, 88, 78, 88, 86, 72, 76),
 ("Yannick Carrasco",    "LW",181, 3, 5, 76, 76, 44, 80, 78, 90, 72),
 ("Angel Correa",        "ST",171, 3, 5, 78, 76, 42, 78, 78, 88, 66),
 ("Saul Niguez",         "CM",184, 3, 3, 66, 82, 78, 76, 82, 76, 84),
 ("Thomas Lemar",        "AM",171, 3, 4, 68, 84, 44, 82, 80, 84, 60),
 ("Mario Hermoso",       "CB",184, 4, 2, 30, 78, 82, 34, 80, 62, 82),
 ("Renan Lodi",          "LB",173, 2, 3, 44, 76, 74, 70, 74, 78, 76),
 ("Joao Felix",          "AM",181, 4, 5, 78, 82, 32, 86, 82, 90, 62)])

squad("Juventus","2019-20","Serie A",[
 ("Cristiano Ronaldo",   "LW",187, 5, 5, 96, 74, 30, 78, 88, 84, 90),
 ("Paulo Dybala",        "AM",177, 3, 5, 88, 86, 34, 92, 88, 92, 66),
 ("Gonzalo Higuain",     "ST",186, 3, 3, 88, 76, 30, 74, 88, 76, 82),
 ("Miralem Pjanic",      "CM",180, 3, 4, 72, 92, 60, 90, 90, 82, 62),
 ("Leonardo Bonucci",    "CB",190, 3, 2, 30, 90, 88, 46, 94, 60, 84),
 ("Matthijs de Ligt",    "CB",189, 3, 2, 34, 82, 88, 34, 84, 64, 92),
 ("Giorgio Chiellini",   "CB",187, 2, 2, 32, 72, 92, 26, 94, 52, 92),
 ("Alex Sandro",         "LB",181, 3, 3, 56, 78, 80, 74, 80, 80, 86),
 ("Juan Cuadrado",       "RB",176, 2, 4, 68, 80, 60, 82, 80, 88, 76),
 ("Blaise Matuidi",      "CM",175, 3, 3, 62, 78, 80, 66, 80, 76, 90),
 ("Rodrigo Bentancur",   "CM",187, 3, 3, 58, 84, 78, 72, 82, 80, 82),
 ("Aaron Ramsey",        "AM",178, 4, 3, 72, 82, 64, 80, 82, 78, 74),
 ("Douglas Costa",       "RW",172, 3, 5, 72, 78, 34, 84, 76, 94, 66),
 ("Danilo",              "RB",184, 3, 3, 50, 78, 78, 70, 80, 76, 82)])

squad("Tottenham Hotspur","2018-19","Premier League",[
 ("Harry Kane",          "ST",188, 4, 3, 95, 82, 32, 84, 92, 66, 84),
 ("Son Heung-min",       "LW",183, 5, 4, 88, 78, 42, 82, 86, 90, 82),
 ("Christian Eriksen",   "AM",182, 3, 3, 76, 94, 46, 96, 92, 82, 58),
 ("Lucas Moura",         "RW",172, 3, 5, 80, 74, 38, 78, 76, 92, 72),
 ("Toby Alderweireld",   "CB",186, 3, 2, 30, 84, 90, 40, 92, 62, 84),
 ("Jan Vertonghen",      "CB",189, 4, 2, 32, 82, 88, 42, 90, 64, 86),
 ("Dele Alli",           "AM",188, 3, 4, 82, 80, 52, 84, 84, 84, 76),
 ("Kieran Trippier",     "RB",178, 2, 3, 50, 88, 76, 90, 84, 72, 74),
 ("Danny Rose",          "LB",173, 2, 3, 46, 74, 78, 70, 76, 78, 84),
 ("Moussa Sissoko",      "CM",187, 3, 3, 54, 76, 78, 66, 76, 78, 94),
 ("Harry Winks",         "CM",178, 3, 3, 46, 86, 70, 76, 86, 78, 62),
 ("Erik Lamela",         "RW",183, 3, 4, 70, 80, 50, 82, 78, 86, 70),
 ("Davinson Sanchez",    "CB",187, 2, 2, 26, 74, 84, 26, 78, 62, 90),
 ("Ben Davies",          "LB",181, 2, 2, 38, 78, 80, 66, 80, 70, 78)])

squad("Napoli","2017-18","Serie A",[
 ("Dries Mertens",       "ST",169, 4, 4, 88, 80, 34, 84, 86, 88, 62),
 ("Lorenzo Insigne",     "LW",163, 2, 5, 84, 86, 36, 90, 88, 92, 56),
 ("Jose Callejon",       "RW",178, 3, 3, 80, 80, 46, 82, 88, 80, 68),
 ("Marek Hamsik",        "CM",183, 4, 4, 78, 88, 60, 88, 90, 84, 76),
 ("Jorginho",            "DM",178, 3, 3, 46, 94, 74, 82, 94, 74, 62),
 ("Kalidou Koulibaly",   "CB",186, 3, 2, 30, 80, 92, 30, 88, 64, 94),
 ("Raul Albiol",         "CB",186, 2, 2, 26, 80, 86, 28, 88, 56, 82),
 ("Faouzi Ghoulam",      "LB",184, 2, 3, 48, 84, 78, 82, 82, 78, 80),
 ("Allan",               "DM",173, 3, 3, 48, 82, 86, 62, 84, 80, 84),
 ("Elseid Hysaj",        "RB",182, 3, 2, 38, 78, 80, 60, 80, 70, 78),
 ("Piotr Zielinski",     "AM",180, 4, 4, 70, 86, 54, 84, 84, 86, 66),
 ("Arkadiusz Milik",     "ST",186, 3, 3, 82, 66, 30, 62, 78, 70, 82),
 ("Mario Rui",           "LB",172, 2, 3, 42, 82, 74, 78, 80, 74, 64),
 ("Amadou Diawara",      "DM",184, 3, 2, 44, 82, 80, 62, 82, 72, 82)])

squad("Sevilla","2019-20","La Liga",[
 ("Lucas Ocampos",       "LW",187, 3, 4, 80, 76, 48, 80, 78, 84, 86),
 ("Youssef En-Nesyri",   "ST",189, 3, 3, 80, 60, 30, 58, 74, 70, 88),
 ("Ever Banega",         "CM",175, 3, 4, 70, 92, 60, 90, 90, 86, 62),
 ("Fernando Reges",      "DM",181, 3, 2, 44, 84, 86, 60, 88, 68, 86),
 ("Diego Carlos",        "CB",185, 2, 2, 32, 74, 88, 28, 82, 62, 92),
 ("Jules Kounde",        "CB",178, 3, 3, 30, 84, 88, 40, 86, 76, 86),
 ("Jesus Navas",         "RB",172, 2, 3, 52, 82, 76, 84, 84, 82, 74),
 ("Sergio Reguilon",     "LB",178, 2, 3, 48, 80, 78, 78, 80, 82, 78),
 ("Suso",                "RW",177, 2, 4, 70, 86, 40, 88, 82, 84, 58),
 ("Joan Jordan",         "CM",185, 3, 3, 62, 84, 72, 78, 82, 74, 78),
 ("Munir El Haddadi",    "ST",176, 3, 4, 74, 70, 32, 68, 74, 82, 66),
 ("Nemanja Gudelj",      "DM",187, 3, 2, 44, 80, 80, 56, 82, 64, 84),
 ("Franco Vazquez",      "AM",184, 4, 4, 70, 84, 50, 82, 82, 82, 74),
 ("Luuk de Jong",        "ST",188, 3, 2, 72, 66, 34, 60, 76, 60, 86)])

squad("Bayer Leverkusen","2015-16","Bundesliga",[
 ("Javier Hernandez",    "ST",175, 3, 3, 88, 62, 28, 60, 86, 74, 72),
 ("Hakan Calhanoglu",    "AM",178, 3, 4, 76, 90, 52, 90, 84, 78, 70),
 ("Karim Bellarabi",     "RW",180, 3, 4, 74, 72, 44, 76, 74, 86, 82),
 ("Kevin Kampl",         "CM",178, 3, 4, 60, 86, 68, 82, 84, 88, 70),
 ("Jonathan Tah",        "CB",195, 3, 2, 24, 76, 84, 26, 78, 58, 90),
 ("Omer Toprak",         "CB",187, 3, 2, 28, 74, 84, 28, 80, 58, 86),
 ("Lars Bender",         "CM",183, 3, 2, 58, 80, 84, 66, 86, 70, 84),
 ("Admir Mehmedi",       "LW",180, 4, 4, 74, 74, 42, 74, 76, 82, 78),
 ("Wendell",             "LB",178, 2, 3, 48, 78, 76, 74, 76, 76, 80),
 ("Benjamin Henrichs",   "RB",184, 3, 3, 46, 76, 76, 68, 76, 78, 78),
 ("Stefan Kiessling",    "ST",191, 3, 2, 80, 66, 32, 62, 80, 62, 86),
 ("Christoph Kramer",    "DM",191, 3, 2, 40, 80, 80, 56, 82, 66, 82),
 ("Julian Brandt",       "LW",185, 4, 4, 72, 84, 42, 84, 82, 84, 62),
 ("Tin Jedvaj",          "CB",184, 3, 2, 28, 72, 78, 30, 74, 62, 80)])

squad("Olympique Lyonnais","2014-15","Ligue 1",[
 ("Alexandre Lacazette", "ST",175, 3, 4, 90, 72, 32, 74, 84, 84, 78),
 ("Nabil Fekir",         "AM",173, 3, 5, 82, 86, 40, 90, 86, 92, 70),
 ("Maxime Gonalons",     "DM",186, 3, 2, 44, 80, 84, 58, 84, 66, 84),
 ("Corentin Tolisso",    "CM",181, 4, 3, 70, 82, 74, 76, 80, 80, 86),
 ("Samuel Umtiti",       "CB",182, 2, 2, 28, 80, 86, 30, 84, 66, 88),
 ("Christophe Jallet",   "RB",183, 3, 2, 46, 76, 76, 70, 78, 72, 78),
 ("Clinton Njie",        "ST",175, 3, 4, 76, 64, 32, 66, 70, 86, 76),
 ("Jordan Ferri",        "CM",178, 3, 3, 58, 82, 70, 76, 80, 76, 70),
 ("Milan Bisevac",       "CB",185, 2, 2, 26, 68, 82, 24, 78, 54, 86),
 ("Henri Bedimo",        "LB",180, 2, 3, 46, 76, 76, 70, 76, 74, 80),
 ("Yoann Gourcuff",      "AM",185, 3, 4, 68, 84, 40, 82, 80, 80, 64),
 ("Steed Malbranque",    "CM",173, 3, 3, 58, 80, 66, 74, 82, 76, 66),
 ("Bakary Kone",         "CB",182, 2, 2, 24, 68, 80, 24, 76, 56, 86),
 ("Rachid Ghezzal",      "RW",180, 2, 4, 68, 78, 40, 78, 76, 84, 62)])

squad("AS Roma","2017-18","Serie A",[
 ("Edin Dzeko",          "ST",193, 4, 3, 88, 78, 34, 74, 88, 68, 88),
 ("Radja Nainggolan",    "CM",176, 3, 3, 76, 84, 82, 82, 86, 80, 90),
 ("Kevin Strootman",     "CM",186, 3, 3, 62, 86, 82, 76, 86, 74, 86),
 ("Kostas Manolas",      "CB",189, 2, 2, 28, 74, 88, 26, 82, 60, 92),
 ("Federico Fazio",      "CB",195, 2, 2, 34, 76, 84, 30, 84, 52, 88),
 ("Aleksandar Kolarov",  "LB",187, 2, 3, 62, 84, 78, 86, 82, 72, 86),
 ("Cengiz Under",        "RW",173, 2, 4, 76, 78, 36, 82, 76, 86, 64),
 ("Stephan El Shaarawy", "LW",178, 3, 4, 80, 74, 38, 78, 78, 86, 72),
 ("Daniele De Rossi",    "DM",184, 4, 2, 62, 86, 86, 68, 92, 64, 86),
 ("Diego Perotti",       "LW",180, 2, 4, 76, 82, 40, 84, 80, 84, 66),
 ("Alessandro Florenzi",  "RB",173, 3, 3, 64, 80, 76, 78, 82, 78, 78),
 ("Lorenzo Pellegrini",  "AM",186, 3, 3, 70, 86, 60, 84, 84, 80, 72),
 ("Bruno Peres",         "RB",178, 3, 3, 52, 72, 72, 70, 72, 80, 82),
 ("Patrik Schick",       "ST",191, 4, 3, 78, 66, 28, 62, 76, 72, 80)])

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
