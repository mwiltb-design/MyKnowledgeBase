Source: [[RV_Park_Designer_Selection.md]], [[RV_Park_Conversion_Design.md]], [[RV_Park_Website_101.md]], [[RV_Park_Integrated_Ecosystem.md]], [[RV_Park_UX_Grunt_Test.md]]

## Summary
- **Decoupled Architecture**: High-performance marketing site (WP/Squarespace) linked via API to specialized booking engines.
- **"Grunt Test" UX**: Headline and sub-headline must communicate value within **3–7 seconds** with persistent "Book Now" CTAs.
- **Mobile-First Performance**: Optimized for travelers on cellular data using high-performance image compression (<200KB).

## Design Architecture
- **Hierarchy**: Prioritize **"Fit First, Amenities Second."** Technical layouts must lead with rig length, turning radius, and slide-out clearance.
- **Modular Structure**: 6-page core (Home, Gallery, Amenities, Activities, Rates, Contact) for optimal indexing.
- **AI Readiness**: Implementation of **`LLMs.txt`** files to manage how AI search engines crawl and process park data.

## Interactive Features
- **Site-Specific Fidelity**: Zoomable maps linked to actual photos of each specific pad and hookup.
- **Navigation**: Persistent, non-moving mobile navigation to prevent "bounce" on small screens.
- **GPS Integration**: Mandatory inclusion of precise coordinates for specialized RV GPS units.

## Tech Stack 2026
- **Frontend**: React (TypeScript) or Compose Multiplatform for cross-device consistency.
- **Backend**: **[[PocketBase]]** (Recommended).
  - **Why**: Single-binary deployment, embedded **[[SQLite]]**, and built-in Auth/File storage are ideal for independent RV park operations with low transactional volume (~60/mo).
- **Search**: **[[RV Park Local SEO]]** is the primary driver; site search should focus on availability and amenities.

---
**See also:** [[PocketBase]], [[RV Park Operations 2026]], [[RV Park Local SEO]], [[A2UI]].
