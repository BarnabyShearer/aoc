defmodule Aoc20251210a do
  def parse_section(<<"[", rest::binary>>),
    do:
      String.split(String.replace(rest, "]", ""), "", trim: true)
      |> Enum.map(fn x -> if x == "#", do: 1, else: 0 end)
      |> Enum.reverse()
      |> Enum.reduce(0, fn x, t -> t * 2 + x end)

  def parse_section(<<"(", rest::binary>>),
    do:
      String.split(String.replace(rest, ")", ""), ",")
      |> Enum.map(&String.to_integer/1)
      |> Enum.reduce(0, fn x, t -> t + 2 ** x end)

  def parse_section(<<"{", _rest::binary>>), do: 0

  def best_subset(nums, target) do
    search(nums, target, 0, [], nil)
  end

  def search([], target, current, subset, best) do
    if current == target and (best == nil or length(subset) < length(best)),
      do: subset,
      else: best
  end

  def search([x | rest], target, current, subset, best) do
    if best != nil and length(subset) >= length(best) do
      best
    else
      search(
        rest,
        target,
        current,
        subset,
        search(
          rest,
          target,
          Bitwise.bxor(current, x),
          [x | subset],
          best
        )
      )
    end
  end

  def parse(line),
    do: String.split(line, " ") |> Enum.map(&parse_section/1) |> (fn [a | b] -> {a, b} end).()

  def call(input) do
    Enum.map(input, &parse/1)
    |> Enum.map(fn {target, buttons} -> Enum.count(best_subset(buttons, target)) end)
    |> Enum.sum()
  end
end
