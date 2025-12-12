defmodule Aoc20251211b do
  def dfs(graph, current, target, visited, met, required, cache) do
    key = {current, met}

    case cache do
      %{^key => cached} ->
        {cached, cache}

      _ ->
        {count, new_cache} =
          _dfs(graph, current, target, visited, met, required, cache)

        {count, Map.put(new_cache, key, count)}
    end
  end

  def _dfs(_graph, target, target, _visited, met, required, cache) do
    if MapSet.subset?(required, met) do
      {1, cache}
    else
      {0, cache}
    end
  end

  def _dfs(graph, current, target, visited, met, required, cache) do
    visited = MapSet.put(visited, current)

    met =
      if MapSet.member?(required, current),
        do: MapSet.put(met, current),
        else: met

    Map.get(graph, current, [])
    |> Enum.reduce({0, cache}, fn n, {acc, acc_cache} ->
      if MapSet.member?(visited, n) do
        {acc, acc_cache}
      else
        {sub, new_cache} =
          dfs(
            graph,
            n,
            target,
            visited,
            met,
            required,
            acc_cache
          )

        {acc + sub, new_cache}
      end
    end)
  end

  def call(input) do
    Enum.map(input, &Aoc20251211a.parse/1)
    |> Map.new(fn [head | tail] -> {String.slice(head, 0..(String.length(head) - 2)), tail} end)
    |> dfs("svr", "out", MapSet.new(), MapSet.new(), MapSet.new(["dac", "fft"]), %{})
    |> elem(0)
  end
end
