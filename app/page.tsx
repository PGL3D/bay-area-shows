import { events } from './data';

export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white p-8">
      <h1 className="text-5xl font-bold mb-8">
        Bay Area Shows
      </h1>

      <div className="space-y-4">
        {events.map((event) => (
          <div 
            key={event.artist}
            className="border border-gray-800 rounded-xl p-6 bg-gray-900"
          >
            <h2 className="text-2xl font-semibold">
              {event.artist}
            </h2>
            
            <p className="text-gray-400 mt-1">
              {event.venue}
            </p>
            
            <p className="text-gray-500 mt-1">
              {event.date}
            </p>
            <p className="text-gray-500 mt-1">
              {event.ticketType} — ${event.price}
            </p>
            <a 
              href={event.ticketUrl}
              target="_blank"
              className="inline-block mt-4 bg-white text-black px-4 py-2 rounded-lg font-medium"
            >
              View Tickets
            </a>
          </div>
        ))}
      </div>
    </main>
  );
}