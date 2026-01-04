def generate_insights(results):
    bottleneck_step = results["bottleneck"]
    avg_time = results["avg_time"][bottleneck_step]
    total_cost = results["total_cost"][bottleneck_step]

    print("\n=== BUSINESS INSIGHTS REPORT ===")
    print(f"🔴 Bottleneck Process Step: {bottleneck_step}")
    print(f"⏱ Average Time Impact: {avg_time} minutes")
    print(f"💰 Total Cost Impact: {total_cost}")

    print("\n📌 Key Insights:")
    print(f"- The '{bottleneck_step}' stage consumes the highest processing time.")
    print("- Causes delays in the overall workflow.")

    print("\n✅ Recommended Actions:")
    print("- Add automation at this step")
    print("- Break this step into smaller parallel tasks")
    print("- Monitor this step daily using KPIs")

    print("\n🎯 Expected Outcome:")
    print("- Reduced delivery delays")
    print("- Lower operational cost")
    print("- Improved customer satisfaction")
