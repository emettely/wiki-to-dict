import pandas as pd
import wikipedia as wiki


def get_df_from_wiki_page(title):
    html = wiki.page(title).html().encode("UTF-8")
    try:
        df = pd.read_html(html)[1]  # Try 2nd table first as most pages contain contents table first
    except IndexError:
        df = pd.read_html(html)[0]
        print(df.to_string())
    return df


def write_wiki_table_to_csv(title):
    filename = title.replace(" ", "_")
    df = get_df_from_wiki_page(title)
    df.to_csv(f"{filename}.csv", columns=df.columns, index_label="id")


def main():
    food_prep_utensils = "List of food preparation utensils"
    write_wiki_table_to_csv(food_prep_utensils)

    cooking_techniques = "List of cooking techniques"
    write_wiki_table_to_csv(cooking_techniques)


if __name__ == '__main__':
    main()
