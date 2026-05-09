"""Check data source health and status."""
from rich.console import Console
from rich.table import Table

from src.healthcheck import run_all_healthchecks

console = Console()


def main() -> None:
    """Run health checks and display results."""
    console.print("\n[bold]Data Source Health Check[/bold]\n")

    results = run_all_healthchecks(symbol="AAPL")

    # Build table
    table = Table(title="Source Status")
    table.add_column("Source", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Message", style="green")

    for result in results:
        status_color = {
            "ok": "[green]ok[/green]",
            "skipped": "[yellow]skipped[/yellow]",
            "error": "[red]error[/red]",
        }.get(result["status"], result["status"])

        table.add_row(
            result["source"],
            status_color,
            result["message"],
        )

    console.print(table)

    # Summary
    ok_count = sum(1 for r in results if r["status"] == "ok")
    skipped_count = sum(1 for r in results if r["status"] == "skipped")
    error_count = sum(1 for r in results if r["status"] == "error")

    console.print(
        f"\n[bold]Summary:[/bold] {ok_count} ok, {skipped_count} skipped, {error_count} error\n"
    )


if __name__ == "__main__":
    main()
