from analysis.process_analysis import run_process_analysis
from agent.insights import generate_insights

def main():
    print("\n🚀 Running AI Business Process Intelligence Agent\n")

    results = run_process_analysis()

    print("\n📊 Analysis Results:")
    for key, value in results.items():
        print(f"{key}: {value}")

    print("\n🧠 AI Insights:")
    generate_insights(results)

    print("\n✅ Execution finished successfully.")

if __name__ == "__main__":
    main()
