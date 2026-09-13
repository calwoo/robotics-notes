# Hardware Buying Guide

> Course: Princeton ROB 345/549, Introduction to Robotics
>
> Offering checked: Fall 2026
>
> Prices and availability checked: 2026-09-13
>
> Currency: USD; shipping, tax, duties, and incidental mounting materials are excluded

## Recommendation at a glance

For the least compatibility risk with the current course, buy the **Crazyflie 2.1 Brushless STEM bundle** for **$550**. It contains all three items named for the motion-planning and control assignments: the brushless Crazyflie, Flow deck v2, and Crazyradio 2.0.

The **Crazyflie 2.1+ STEM drone bundle** is the practical budget alternative at **$320**. It includes the same radio and Flow deck, and the 2.1+ is the direct successor to the brushed Crazyflie used by the course from 2021 through 2025. However, it is not the aircraft specified for Fall 2026. Its lower payload capacity and different firmware target create some risk for later assignments and the camera project.

If taking the course concurrently, buy only the core flight bundle now. Wait for the final-project instructions before ordering the camera, long pins, or custom mounting supplies.

## Current-course purchase list

### Buy now: exact Fall 2026 configuration

| Item | What it supplies | Price | Source |
|---|---|---:|---|
| Crazyflie 2.1 Brushless STEM bundle | Crazyflie 2.1 Brushless, Flow deck v2, Crazyradio 2.0, battery, USB cable, propeller guards, and basic spares | $550.00 | [Bitcraze](https://store.bitcraze.io/products/stem-bundle-crazyflie-2-1-brushless) |
| **Core total** | Everything publicly listed for motion planning and control | **$550.00** | |

Buying the three principal components separately would currently cost about **$578**: $480 for the aircraft, $55 for the Flow deck, and $43 for Crazyradio 2.0. The bundle saves about $28 and reduces the chance of omitting a component.

The course page names the older Crazyradio PA, but Bitcraze identifies it as a discontinued product replaced by Crazyradio 2.0. The bundle's Crazyradio 2.0 is therefore the appropriate current purchase.

### Buy later: final-project hardware

| Item | Price | Source | Purchase note |
|---|---:|---|---|
| Seeed Studio XIAO ESP32-S3 Sense | $13.90 | [Seeed Studio](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html) or the [course-linked Amazon listing](https://www.amazon.com/dp/B0C69FFVHH) | The current course labels its link "Digital FPV camera," but the linked product is this digital camera/microcontroller board. Amazon's price may differ. |
| Long Pins, 15+4+6 mm, pack of four | $2.00 | [Bitcraze](https://store.bitcraze.io/products/long-pins-1546) | Likely replacement for the course's stale long-pins link; confirm the released mounting instructions before ordering. |
| Mounting and wiring materials | Not yet known | Wait for project instructions | The public page does not yet specify a mount, cable, connector, or fastener bill of materials. |
| **Estimated final-project add-on subtotal** | **$15.90 plus mounting materials** | | |

**Estimated exact-course total: $565.90 plus shipping, tax, duties, and mounting materials.**

## Lower-cost route: Crazyflie 2.1+

| Item | What it supplies | Price | Source |
|---|---|---:|---|
| STEM drone bundle – Crazyflie 2.1+ | Crazyflie 2.1+, Flow deck v2, Crazyradio 2.0, battery, and micro-USB cable | $320.00 | [Bitcraze](https://store.bitcraze.io/collections/bundles-crazyflie-2-1/products/stem-drone-bundle) |
| Later camera and long pins | Same provisional final-project items as above | $15.90 | [Seeed Studio](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html) and [Bitcraze](https://store.bitcraze.io/products/long-pins-1546) |
| **Estimated budget total** | Excludes unknown mounting materials | **$335.90** | |

Why it is plausible:

- The 2.1+ supports the Flow deck v2 and the same Crazyradio ecosystem.
- The course's Fall 2023, 2024, and 2025 repositories target the original brushed Crazyflie 2.1; the current 2.1+ is its successor.
- Its bundle already contains the core equipment needed for the archived planning and control labs.

Why it is not a drop-in guarantee for Fall 2026:

- The current course explicitly specifies the Crazyflie 2.1 Brushless.
- The 2.1+ has a recommended payload of 15 g, versus 40 g for the brushless model. After the 1.6 g Flow deck and approximately 0.7 g long pins, only about 12.7 g remains for the camera, wiring, and mount.
- Typical advertised flight time is about 7 minutes for the 2.1+, versus 10 minutes for the brushless model; camera power and added weight will reduce it further.
- The platforms use different firmware build targets (`cf2` and `cf21bl`). A released lab may include gains, thrust values, or scripts tuned specifically for the brushless aircraft.

**Bottom line:** choose the $320 bundle for self-study or if saving $230 is worth possible adaptation work. Choose the $550 brushless bundle when assignment compatibility matters more than price.

## Sensible optional spares

These are convenience purchases, not items presently required by the public course page.

| Item | Fits | Price | Source | When it is useful |
|---|---|---:|---|---|
| Extra 350 mAh LiPo battery | Brushless | $12.00 | [Bitcraze](https://store.bitcraze.io/products/350mah-lipo-battery) | Longer lab sessions while another battery charges |
| Extra 250 mAh LiPo battery | 2.1+ | $6.50 | [Bitcraze](https://store.bitcraze.io/products/250mah-lipo-battery) | Same reason; use the battery intended for the lighter airframe |
| Brushless 55-35 propeller pack | Brushless | $6.00 | [Bitcraze](https://store.bitcraze.io/products/propeller-55-35-4ccw-4cw-black) | Cheap insurance after crashes; includes four clockwise and four counter-clockwise props |
| 47-17 propeller pack | 2.1+ | About $6.00 | [Bitcraze spare-parts collection](https://store.bitcraze.io/collections/spare-parts-crazyflie-2-0) | Replacement props for the brushed platform |

The included battery charges through the Crazyflie's USB connection, so a separate charger is not necessary for the initial purchase. Bitcraze warns that shipping more than two spare batteries per Crazyflie can trigger additional dangerous-goods handling fees; compare the delivered cost before adding several batteries.

## Do not buy yet

- Do not buy both Crazyradio PA and Crazyradio 2.0. Buy the current 2.0 replacement.
- Do not add a Lighthouse deck, Loco Positioning deck, Multi-ranger deck, or AI deck. None is listed in the current public bill of materials.
- Do not buy a separate USB cable or charger for a one-battery setup; the bundles include the appropriate cable, and the aircraft charges the battery.
- Do not buy the historical WT05 analog camera and Skydroid receiver unless intentionally reproducing the 2021–2025 vision labs. Fall 2026 points to a different digital camera board.

## Where to source the parts

Bitcraze's own store is the safest source for the aircraft, deck, radio, pins, batteries, and airframe-specific spares because its product pages document compatibility and bundle contents. Compare its checkout total against a local authorized reseller if international shipping or import duties are significant, but match the exact product revision and contents before ordering.

Buy the XIAO ESP32-S3 Sense from Seeed Studio or the course-linked Amazon listing. The Seeed listing is the clearer reference for the exact board revision; Amazon may offer faster domestic fulfillment.

## Historical context

The Fall 2021 course launch and the public Fall 2023–2025 repositories used the original brushed Crazyflie 2.1, Flow deck, and Crazyradio. The 2024 and 2025 lab notebooks build or flash the `cf2` firmware target. Those offerings also used a WT05 analog camera and Skydroid receiver for vision work. The current Fall 2026 page is the first public course version in this series to list the Crazyflie 2.1 Brushless and the XIAO-based digital camera board.

This history supports the 2.1+ as a strong choice for following archived assignments, but it does not establish compatibility with every unreleased Fall 2026 lab.

## Price-refresh checklist

Before checkout:

1. Re-open the [current course page](https://irom-lab.princeton.edu/intro-to-robotics/) and check for newly released assignment hardware notes.
2. Confirm that the selected bundle includes the aircraft, Flow deck v2, and Crazyradio 2.0.
3. Recalculate the delivered total with shipping, tax, and duties.
4. If choosing the 2.1+, weigh the complete camera, wiring, pins, and mount before flight and keep the assembly within the airframe's payload guidance.

## Primary sources

- [Princeton ROB 345/549 course page](https://irom-lab.princeton.edu/intro-to-robotics/)
- [Bitcraze: Crazyflie 2.1 Brushless STEM bundle](https://store.bitcraze.io/products/stem-bundle-crazyflie-2-1-brushless)
- [Bitcraze: Crazyflie 2.1+ STEM drone bundle](https://store.bitcraze.io/collections/bundles-crazyflie-2-1/products/stem-drone-bundle)
- [Bitcraze: Crazyflie 2.1 Brushless](https://store.bitcraze.io/products/crazyflie-2-1-brushless)
- [Bitcraze: Crazyflie 2.1+](https://store.bitcraze.io/collections/kits/products/crazyflie-2-1-plus)
- [Bitcraze: Flow deck v2](https://store.bitcraze.io/products/flow-deck-v2)
- [Bitcraze: Crazyradio 2.0](https://store.bitcraze.io/products/crazyradio-2-0)
- [Bitcraze: Princeton course launch, Fall 2021](https://www.bitcraze.io/2022/01/introduction-to-robotics-at-princeton/)
- [Princeton Introduction to Robotics repositories](https://github.com/Princeton-Introduction-to-Robotics)
- [Seeed Studio: XIAO ESP32-S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)

## Uncertainty note

Only the first assignment is public at the time of this check. The final-project camera link is identifiable, but the complete mechanical and electrical integration instructions are not. Prices, stock, and course requirements may change; the totals above are a planning estimate rather than an official course quote.
