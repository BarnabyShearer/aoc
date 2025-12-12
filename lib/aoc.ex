defmodule Aoc do
  def main(args) do
    options = OptionParser.parse(args, strict: [day: :string, part_two: :boolean]) |> elem(0)

    day =
      if options[:day] do
        options[:day]
      else
        today = DateTime.utc_now()

        "#{today.year}#{String.pad_leading(Integer.to_string(today.month), 2, "0")}#{String.pad_leading(Integer.to_string(today.day), 2, "0")}"
      end

    day_module =
      String.to_existing_atom("Elixir.Aoc" <> day <> if(options[:part_two], do: "b", else: "a"))

    input =
      Req.get!(
        "https://adventofcode.com/#{String.slice(day, 0..3)}/day/#{String.slice(day, 6..7) |> Integer.parse() |> elem(0)}/input",
        headers: [{"cookie", "session=#{System.get_env("AOC_SESSION")}"}]
      ).body
      |> String.split("\n", trim: true)

    apply(day_module, :call, [input])
    |> IO.inspect(charlists: :as_lists)
  end
end
