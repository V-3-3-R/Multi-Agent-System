from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic : str) -> dict:

    state = {}
    # Step 1: Search Agent gathers information
    print("\n" + "="*50)
    print("Step 1: Search Agent is working...")
    print("="*50 )
    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        "messages" : [("user", f"Find recent, reliable and detailed information on the topic: {topic}.")]
    })
    state["search_results"] = search_results['messages'][-1].content
    print(f"Search Results:\n{state['search_results']}")


    # Step 2: Reader Agent digs deeper into the URLs found
    print("\n" + "="*50)
    print("Step 2: Reader Agent is working...")
    print("="*50 )
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages" : [("user", 
            f"Based on the following search results about '{topic},"
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content
    print(f"Scraped Content:\n{state['scraped_content']}")

    # Step 3: Writer Chain compiles a research report
    print("\n" + "="*50)
    print("Step 3: Writer is drafting a report...")
    print("="*50 )

    research_combined = (
        f"Search Results:\n{state['search_results']}\n\n"
        f"Detailed Scraped Content:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print(f"Final Drafted Report:\n{state['report']}")

    # Step 4: Critic Chain evaluates the report
    print("\n" + "="*50)
    print("Step 4: Critic is evaluating the report...")
    print("="*50 )

    state["Feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print(f"Feedback:\n{state['Feedback']}")

    return state

if __name__ == "__main__":
    topic = input("\n Enter a research topic: ")
    run_research_pipeline(topic)
