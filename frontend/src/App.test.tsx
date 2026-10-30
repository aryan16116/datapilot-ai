import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi, beforeEach } from "vitest";
import App from "./App";

describe("App", () => {
  beforeEach(() => {
    vi.stubGlobal(
      "fetch",
      vi.fn(() =>
        Promise.resolve(new Response(JSON.stringify({ status: "ok" }), { status: 200 })),
      ),
    );
  });

  it("shows backend ok after a successful health check", async () => {
    render(<App />);
    expect(await screen.findByText("Backend status: ok")).toBeInTheDocument();
  });
});