defmodule Aoc20251210b do
  def parse(line) do
    [_d | rest] = String.split(line, " ", trim: true)

    Enum.map(rest, fn s ->
      String.split(String.slice(s, 1..(String.length(s) - 2)), ",")
      |> Enum.map(&String.to_integer/1)
    end)
    |> List.pop_at(-1)
  end

  def lp_solve(lp_text) do
    # WTF is lp_solve doing to pipes?
    case System.cmd("bash", ["-c", "lp_solve -S1 <<< \"$INPUT\""], env: [{"INPUT", lp_text}]) do
      {output, 0} ->
        Regex.run(~r/(\d+)\./, output) |> List.last() |> String.to_integer()
    end
  end

  def solve({targets, buttons}) do
    lp_solve("""
    min: #{Enum.map(0..(length(buttons) - 1), fn v -> "v#{v}" end) |> Enum.join(" + ")};
    #{Enum.with_index(targets) |> Enum.map(fn {t, i} -> (Enum.with_index(buttons) |> Enum.filter(fn {b, _} -> Enum.member?(b, i) end) |> Enum.map(fn {_, v} -> "v#{v}" end) |> Enum.join(" + ")) <> " = #{t};" end) |> Enum.join("\n")}
    int #{Enum.map(0..(length(buttons) - 1), fn v -> "v#{v}" end) |> Enum.join(", ")};
    """)
  end

  def call(input) do
    Enum.map(input, &parse/1)
    |> Enum.map(&solve/1)
    |> Enum.sum()
  end
end
