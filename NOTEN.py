#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:38:58 2025

@author: cvetkofabian
"""


TBD = None # Platzhalter


sem1 = {
        "pro1M" : [[(5.5, 0.1, "Konzeptskizze"), (5.8, 0.15, "Sitzungsprotokolle"), (4.9, 0.2, "Reflexionsbericht"), (5.3, 0.15, "Fertigungszeichnung"), (5, 0.15, "Bericht Teil: Sprachkompetenz"), (4.8, 0.15, "Bericht Teil: Konstruktion"), (5.5, 0.1, "Präsentation")], [None]],
        "an1"   : [[4.6, 4.4, (5.1, 1, "Bonus +0.2 Note für Python-Aufgabe Newton-Verfahren")], [4.9]],
        "mechM" : [[5, 3.5, 5], [5.2]],
        "lalg1" : [[4.2, 4.7], [4.7]],
        "esfss" : [[(5.58, 0.6, "Presentation"), (5.35, 0.4, "Final Exam")], [None]],
        "AuA"   : [[(5.8, 0.5, "1-Minuten-Rede"), (5.2, 0.2, "Analyse Auftritt"), (4.5, 0.3, "Podium")], [None]],
        "infM"  : [[(6.1, 0.5), (5.4, 0.25, "Projekt"), (5.6, 0.25, "Projekt")], [None]],
        "werk"  : [[5.4, 4.8], [None]],
        "ch1"   : [[4.5], [4.3]],
        "hkon"  : [[(4.65, 0.5, "Teil Herstellung"), (6, 0.2, "Teil Konstruktion Peergrading Zeichnung"), (4.6, 0.3, "Teil Konstruktion")], [None]]
        }


sem2 = {
        "pro2M" : [[(5.75, 0.1, "Sitzungsmoderation"), (4.5, 0.15, "Patentrecherche"), (4.8, 0.15, "Technischer Bericht Sprachkompetenz"), (4.9, 0.2, "Zeichnungssatz")], [None]],
        "thdM"  : [[4.5], [3.5]],
        "an2"   : [[4.9, 4, (5.06, 1, "Bonus +0.2 Note für Python-Aufgabe")], [4.3]],
        "lalg2" : [[(5.2, 2), (4.7, 1)], [None]],
        "chkL"  : [[(5.1, 0.25, "Chemie Schriftliche Prüfung"), (5.166, 0.125, "Chemiepräsentation"), (4.333, 0.125, "Chemie-Laborbericht"), (5, 0.5, "CADA-Challenge-und-Präsentation")], [None]],
        "stk"   : [[5.18, 4.2], [None]],
        "wisa"  : [[5], [None]],
        "wus"   : [[3.8, 4.8], [4]],
        "mel"   : [[(3.45, 1), (3.95, 1), (4.88, 1.25)], [None]],
        "eidpe" : [[(6, 0.1, "Moodle Exercises"), (5.5, 0.4, "Poster and Canvas"), (4.5, 0.5, "Pitch")], [None]],
        "werk2" : [[3.72], [4.9]],
       }


sem3 = {
        "pro3M" : [[(5, 1, "Abgabe A"), (5, 1.5, "Abgabe B"), (5.1, 2.5, "Abgabe D (Einzelarbeit)"), (5, 2, "Abgabe E")], [None]],
        "lean"  : [[(5.8, 0.4, "Schriftliche Prüfung"), (TBD, 0.6, "Präsentation & Prozessdokumentation")], [None]],
        "bplan" : [[(5.8, 0.3, "Schriftliche Prüfung"), (TBD, 0.4, "Businessplan-Reasoning & Anhang"), (TBD, 0.3, "Elevator-Pitch & Q&A")], [None]],
        "kmk"   : [[4.8, 3.5], [None]],
        "eltM"  : [[(6, 0.15, "Labor 1"), (4.3, 0.7, "Schriftliche Prüfung"), (TBD, 0.15, "Labor 2")], [TBD]],
        "elstk" : [[4.2], [TBD]],
        "num"   : [[5.5, 3.3], [None]],
        "flmM"  : [[3], [TBD]]
       }

sem4 = {
        "pro4M" : [[], [None]],
        "md"    : [[], [TBD]],
        "fems"  : [[], [None]],
        "atL"   : [[], [None]],
        "egts"  : [[], [TBD]],
        "man"   : [[], [TBD]],
        "wst"   : [[], [TBD]],
        "ffup"  : [[], [None]],
        "ereth" : [[], [None]],
        "rukg"  : [[], [None]]
       }

sem5 = {
        "pro5M" : [[], [None]]
        # TBD
       }

sem6 = {
        "pro6Ma": [[], [None]]
        # TBD
       }

sem7 = {
        # TBD
       }




def round_half_up(number, decimals=0):
    multiplier = 10**decimals
    return int(number * multiplier + 0.5) / multiplier


def average(grades, round_average = False):
    if grades == [] or grades == [None] or grades == None:
        return None

    grades_weighted = []
    grades_weights = []
    for grade in grades:
        if grade is None:                 # None Platzhalter überspringen
            continue
        if type(grade) == tuple:
            if grade[0] is None:          # None Platzhalter überspringen
                continue
            grades_weights.append(grade[1])
            grade = grade[0] * grade[1]
        else:
            grades_weights.append(1)
        grades_weighted.append(grade)
    if sum(grades_weights) == 0:          # None Platzhalter überspringen: -> Schutz vor Division durch 0
        return None
    weight_total = sum(grades_weights)
    average = sum(grades_weighted) * 1/weight_total
    if round_average != False:
        return round_half_up(average, round_average)
    return average


def grades(semester):
    modules = list(semester.keys())
    results = {}
    for module in modules:
        grades_semester = semester[module][0]
        grades_final_exam = semester[module][1]

        average_semester = average(grades_semester, round_average=1)
        average_final_exam = average(grades_final_exam, round_average=1)

        averages = []
        if average_semester != None:
            averages.append(average_semester)
        if average_final_exam != None:
            averages.append(average_final_exam)

        if len(averages) != 0:
            average_total = round_half_up(sum(averages) / len(averages), 1)
        else:
            average_total = None

        results[module] = (average_semester, average_final_exam, average_total)
    return results




def print_table_tabulate(results_dict, title = None):
    """
    Ausgabe einer Tabelle.
    Eingabe: grades(grades_dict), title="Titel"
    """
    from tabulate import tabulate

    # Titel
    if title == None:
        title = "Modul"

    # Definition
    table = [(key, *value) for key, value in results_dict.items()]
    headers = [title, "Erfa", "MSP", "Final"]

    # Ausgabe Tabelle in Konsole
    print(tabulate(table, headers=headers, tablefmt="grid", colalign=("left", "right", "right", "right")))


def print_table_rich(results_dict, title=None):
    """
    Ausgabe einer formatierten Tabelle.
    Eingabe: grades(grades_dict), title="Titel"
    """
    from rich.table import Table
    from rich.console import Console

    # Titel
    console = Console()
    if title != None:
        table = Table(title=title)

    # Spalten definieren
    table.add_column("Modul  ", style="bold", justify="left")
    table.add_column("Erfa ", justify="right")
    table.add_column("MSP  ", justify="right")
    table.add_column("Final", justify="right")

    # Mit Farben Formatieren
    def format_grade(val):
        if val is None:
            return "-"
        if val < 3.75:
            return f"[red]{val:.1f}[/red]"
        elif val < 4.0:
            return f"[yellow]{val:.1f}[/yellow]"
        else:
            return f"[green]{val:.1f}[/green]"

    # Tabellieren
    for module, (average_semester, average_final_exam, average_total) in results_dict.items():
        table.add_row(
            module,
            format_grade(average_semester),
            format_grade(average_final_exam),
            format_grade(average_total))

    # Ausgabe Tabelle in Konsole
    print("")
    console.print(table)




# Abruf Tabellen
print_table_rich(grades(sem1), "Sem. 1")
print_table_rich(grades(sem2), "Sem. 2")
print_table_rich(grades(sem3), "Sem. 3")
print_table_rich(grades(sem4), "Sem. 4")
"""
print_table_rich(grades(sem5), "Sem. 5")
print_table_rich(grades(sem6), "Sem. 6")
print_table_rich(grades(sem7), "Sem. 7")
"""




# input("\n\nPress Enter to quit...\n")
