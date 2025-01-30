from fuzzywuzzy import process

def match_entities(entity_type: str, transfermarkt_data: dict, sofascore_data: dict):
    """
    Matches entities (championships, teams, players) from Transfermarkt with corresponding entities in Sofascore 
    using fuzzy string matching. If the match score is below a certain threshold, 
    the user is prompted to manually validate or correct the match.

    Parameters:
    -----------
    entity_type : str
        The type of entity being matched (e.g., "championship", "team", "player").
    transfermarkt_data : dict
        Dictionary containing entity names as keys and metadata (ID, country, league, etc.) as values from Transfermarkt.
    sofascore_data : dict
        Dictionary containing entity names as keys and metadata from Sofascore.

    Returns:
    --------
    dict
        A dictionary mapping Transfermarkt entity names to their corresponding Sofascore entity names.
    """

    matched_entities  = {}
    print(f"\n🔄 Matching {entity_type}s...")

    for transfermarkt_name in transfermarkt_data.keys():
        best_match, score = process.extractOne(transfermarkt_name, sofascore_data.keys())

        if score > 80:
            matched_entities[transfermarkt_name] = best_match
        else:
            print(f"\n⚠️ Manual Check Needed for {entity_type}:")
            print(f"   - Transfermarkt: {transfermarkt_name}")
            print(f"   - Closest Sofascore Match: {best_match} (Score: {score})")
            print(f"   - Transfermarkt Data: {transfermarkt_data[transfermarkt_name]}")
            print(f"   - Sofascore Data: {sofascore_data.get(best_match, 'Not Found')}\n")

            user_input = input(f"✅ Accept this match for {entity_type}? (yes/no/custom): ").strip().lower()

            if user_input == "yes":
                matched_entities[transfermarkt_name] = best_match
                print(f"✔️ Matched {entity_type}: {transfermarkt_name} -> {best_match}")
            elif user_input == "custom":
                custom_name = input(f"✏️ Enter the correct {entity_type} name for '{transfermarkt_name}': ").strip()
                if custom_name in sofascore_data:
                    matched_entities[transfermarkt_name] = custom_name
                    print(f"✔️ Custom Matched {entity_type}: {transfermarkt_name} -> {custom_name}")
                else:
                    print(f"❌ Invalid input. Skipping {entity_type}.")
            else:
                print(f"❌ Skipping {entity_type}: {transfermarkt_name}")

    print(f"\n✅ Finished matching {entity_type}s.")
    return matched_entities